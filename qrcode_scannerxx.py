import cv2
from pyzbar import pyzbar
from datetime import date, datetime

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        print (barcode_info)
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        #3
        with open("qrcode_scanned.txt", mode ='w') as file:
            file.write("Recognized QR Code:" + barcode_info)
            current_time = datetime.now()
            time_date = current_time.strftime("%d/%m/%Y %H:%M:%S")
            print(f"Read at {time_date}")
            file.write(f"\n Read at {time_date}")

    return frame

def main():
#for camera
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('QR Code Reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()