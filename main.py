import time

import view, model

while True:
    time.sleep(1/60)
    model.drive_rect()
    view.background()

