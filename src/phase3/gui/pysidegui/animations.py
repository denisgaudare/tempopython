from PySide6.QtCore import QPropertyAnimation

def fade_in_widget(widget, duration=600):
    widget.setWindowOpacity(0)
    widget.show()

    anim = QPropertyAnimation(widget, b"windowOpacity")
    anim.setDuration(duration)
    anim.setStartValue(0)
    anim.setEndValue(1)
    anim.start()
    # Stocker l'animation pour éviter que le GC la tue
    widget._fade_animation = anim
