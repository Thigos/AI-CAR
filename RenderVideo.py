import cv2
import numpy as np
from darkflow.net.build import TFNet
import time

cap = cv2.VideoCapture("estrada.mp4")
larguraCap, alturaCap = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('videoRender.mp4', fourcc, 20.0, (larguraCap, alturaCap))

options = {
    'model': 'cfg/tiny-yolo-voc-2c.cfg',
    'load':6750,
    'threshold': 0.6,
    'gpu': 1.0
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]



print("Dimensões do Video: ",larguraCap,alturaCap)

print("\n*Renderizando Video*\n")
stime = time.time()

while True:
    _,frame = cap.read()
    if(not _):
        break;
    results = tfnet.return_predict(frame)

    for color, result in zip(colors, results):
        tl = (result['topleft']['x'], result['topleft']['y'])
        br = (result['bottomright']['x'], result['bottomright']['y'])

        label = result['label']

        #distance calculator
        largura = br[0] - tl[0]
        distancia = larguraCap/largura
        

        confidence = result['confidence']
        frame = cv2.line(frame, tl, br, color, 5)
        frame = cv2.putText(frame, label + ' C: {:.2f}'.format(confidence), tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
        localTxt = tl[0], br[1]
        frame = cv2.putText(frame, 'D: {:.0f}m'.format(distancia), localTxt, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)

    #frame = cv2.putText(frame, 'FPS {:.1f}'.format(1 / (time.time() - stime)), (10,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)    
    out.write(frame)
    

out.release()
print("Render: ", time.time() - stime)