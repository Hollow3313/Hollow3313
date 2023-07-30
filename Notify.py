import notifypy


Title = input("Title: ")
Text = input("Text: ")
Icon = input("Icon: ")

notification = notifypy.Notify()
notification.title = Title
notification.message = Text
notification.icon = Icon
notification.send()


