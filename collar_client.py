'''
Суть программы заключается в том чтобы делать, в заданый интервал, скриншоты и фото с веб камеры и 
отпровлять это определенный файл на Ftp сервер
'''
import msvcrt
import time
import datetime
import os
#словарь для подключения к ftp
ftp_udifikashen = {
    'ftp_url' : 'f999143o.beget.tech',
    'ftp_login' : 'f999143o_111',
    'ftp_pass' : 'svem9Se'
    }

def otravka_na_ftp (): #отправляем изображения на ftp
    from ftplib import FTP
    from pathlib import Path
    for name_fail_scr_cam in ['scr_' + screenshotd + '.jpg', 'cam_' + screenshotd + '.png']:
        file_path = Path(name_fail_scr_cam)
        with FTP(ftp_udifikashen['ftp_url'], ftp_udifikashen['ftp_login'], ftp_udifikashen['ftp_pass']) as ftp, open(file_path, 'rb') as file:
                ftp.storbinary(f'STOR {file_path.name}', file)
        if 'scr' in name_fail_scr_cam:
                print('Скриншот отправлен')
        else:
                print('Фото с вебкамеры отправлено')
    #Удаляем файл
    for name_fail_scr_cam_del in ['scr_' + screenshotd + '.png', 'cam_' + screenshotd + '.png']:
        os.remove(name_fail_scr_cam_del)

def skrin_and_campoto_name_dete (): #функция делает скриншот с экрана и присваевает именам файлов текщую дату
    import cv2     #чтоб cv2 заработало по виртуальным окружением вбей сие python -m pip install  opencv-python
    #import pyautogui
    #делаем скриншот с экрана
    screen = pyautogui.screenshot('scr_' + screenshotd + '.jpg')
    #Делаем снимок с камеры
    # Включаем первую камеру
    cap = cv2.VideoCapture(0)
    # "Прогреваем" камеру, чтобы снимок не был тёмным
    for i in range(30):
        cap.read()
    # Делаем снимок    
    ret, frame = cap.read()
    # Записываем в файл
    cv2.imwrite('cam_' + screenshotd + '.png', frame)   
    # Отключаем камеру
    cap.release()
user_login = input ('Введите свой логин: ')
user_password = input ('Введите  свой пароль: ')
user_task = input ("Введите задачу которую вы сейчас будете решать: ")
user_time_start_sessia = datetime.datetime.now().strftime('%Y.%m.%d в %H:%M:%S')
user_obalyt_time_start_sessia = time.time() #Переменная дающая нам точку остчета старта сессии
print ('Пользователь ' + user_login + ' приступпил к выполенинию задачи \"' + user_task + '\" ' + user_time_start_sessia)
while not msvcrt.kbhit():
    #Узнаем дату и присваиваем ей переменную
    screenshotd = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #функция делает скриншот с экрана и присваевает именам файлов текщую дату
    skrin_and_campoto_name_dete ()
    #отправляем изображения на ftp
    otravka_na_ftp ()
    #Ждем время 
    time.sleep(3)
    #Переменная текущая точка
    user_obalyt_time_tekyshaia_tochra_sessia = time.time() 
    #сколько отработано по текущей задаче
    user_vi_otrabotali = user_obalyt_time_tekyshaia_tochra_sessia - user_obalyt_time_start_sessia 
    print ('Вы отработали по текущей задаче: ' + str(user_vi_otrabotali) + ' секунд')
