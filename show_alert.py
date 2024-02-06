
from plyer import notification
notification._default_notification_implementation = 'pyqt5'



def show_alert():
    notification.notify(
        title='アラート',
        message='60秒間変更がありませんでした。'
    )
