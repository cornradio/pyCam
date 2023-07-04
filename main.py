# source venv/bin/activate
import datetime
import cv2

# 打开默认的摄像头
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
print("空格 拍照\no 打开目录")
while True:
    # 读取摄像头捕获的视频帧
    ret, frame = cap.read()
    # 显示视频帧
    cv2.imshow('Py Camera', frame)
    # 拍照片
    key = cv2.waitKey(10)
    if key == ord(' '):
        # 显示视频帧
        cv2.imshow('Py Camera', frame)
        # 获取当前时间并将其格式化为字符串
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
        # 将当前帧保存为图像文件
        filename = f'photo_{timestamp}.jpg'
        cv2.imwrite(filename, frame)
        print("save : "+filename)
        # 在屏幕上闪白光
        flash = cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (255, 255, 255), -1)
        cv2.imshow('Py Camera', flash)
        cv2.waitKey(20)
    # 打开文件夹
    elif key == ord('o'):
        import os
        import platform

        # 获取当前工作目录
        current_directory = os.getcwd()

        # 获取当前操作系统名称
        os_name = platform.system()

        # 根据操作系统名称打开文件
        if os_name == 'Windows':
            os.startfile(current_directory)
        elif os_name == 'Linux':
            os.system('xdg-open "{}"'.format(current_directory))
        elif os_name == 'Darwin':
            os.system('open "{}"'.format(current_directory))
        else:
            print('Unsupported operating system')
