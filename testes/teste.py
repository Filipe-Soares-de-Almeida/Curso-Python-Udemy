from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout
)
from PySide6.QtGui import QMouseEvent, QCursor
from PySide6.QtCore import Qt, QRect

import ctypes
import sys


class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(40)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 10, 0)

        self.title = QLabel("🔥 Janela do Guerreiro 🔥")
        self.title.setStyleSheet("color: white; font-weight: bold; font-size: 16px;")
        layout.addWidget(self.title)

        layout.addStretch()

        self.min_btn = QPushButton("—")
        self.max_btn = QPushButton("⬜")
        self.close_btn = QPushButton("✕")

        for btn in (self.min_btn, self.max_btn, self.close_btn):
            btn.setFixedSize(30, 30)
            btn.setStyleSheet("""
              QPushButton {
                background-color: rgba(255,255,255,0.1);
                color: white;
                border: none;
                border-radius: 5px;
              }
              QPushButton:hover {
                background-color: rgba(255,255,255,0.3);
              }
            """)
            layout.addWidget(btn)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setMinimumSize(300, 200)
        self.setGeometry(100, 100, 500, 400)
        self.is_maximized = False
        self.setMouseTracking(True)

        self.container = QWidget()
        self.container.setObjectName("container")
        self.container.setStyleSheet("""
          QWidget#container {
            background-color: rgba(40, 40, 40, 5);
          }
        """)

        self.title_bar = CustomTitleBar(self)
        self.title_bar.min_btn.clicked.connect(self.showMinimized)
        self.title_bar.max_btn.clicked.connect(self.toggle_max_restore)
        self.title_bar.close_btn.clicked.connect(self.close)
        self.title_bar.setMouseTracking(True);

        self.main_content = QLabel("🌫️ Conteúdo da Janela com Blur Fosco e Redimensionamento 🪞")
        # self.main_content.setStyleSheet("color: white; font-size: 18px; padding: 20px;")
        self.main_content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_content.setMouseTracking(True)

        self.vblayout = QVBoxLayout(self.container)
        self.vblayout.setContentsMargins(0, 0, 0, 0)
        self.vblayout.setSpacing(0)
        self.vblayout.addWidget(self.title_bar)
        self.vblayout.addWidget(self.main_content, 1)

        self.setCentralWidget(self.container)

        self._resize_margin = 10
        self._resize_direction = None
        self._resize_start = None
        self._original_geometry = QRect()


        self.enable_blur_effect()

    def toggle_max_restore(self):
        if self.is_maximized:
            self.showNormal()
            self.enable_blur_effect()
        else:
            self.showMaximized()
        self.is_maximized = not self.is_maximized

    def enable_blur_effect(self):
        hwnd = int(self.winId())

        class ACCENTPOLICY(ctypes.Structure):
            _fields_ = [
                ("AccentState", ctypes.c_int),
                ("AccentFlags", ctypes.c_int),
                ("GradientColor", ctypes.c_int),
                ("AnimationId", ctypes.c_int)
            ]

        class WINCOMPATTRDATA(ctypes.Structure):
            _fields_ = [
                ("Attribute", ctypes.c_int),
                ("Data", ctypes.c_void_p),
                ("SizeOfData", ctypes.c_size_t)
            ]

        accent = ACCENTPOLICY()
        accent.AccentState = 4
        accent.AccentFlags = 0x20 | 0x40
        accent.GradientColor = 0x01000000
        accent.AnimationId = 0

        data = WINCOMPATTRDATA()
        data.Attribute = 19
        data.Data = ctypes.addressof(accent)
        data.SizeOfData = ctypes.sizeof(accent)

        ctypes.windll.user32.SetWindowCompositionAttribute(hwnd, ctypes.byref(data))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.position().toPoint()
            if pos.y() < self.title_bar.height():
                self.old_pos = event.globalPosition().toPoint()
            else:
                self._resize_direction = self.get_resize_direction(pos)
                self._resize_start = event.globalPosition().toPoint()
                self._original_geometry = QRect(self.geometry()) 

    def mouseMoveEvent(self, event):
        if hasattr(self, 'old_pos') and self.old_pos:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()
        elif self._resize_direction:
            screen_rect = QApplication.primaryScreen().availableGeometry()
            current_pos = event.globalPosition().toPoint()
            delta = current_pos - self._resize_start

            new_geo = QRect(self._original_geometry)  

            min_width = self.minimumWidth()
            min_height = self.minimumHeight()

            if 'left' in self._resize_direction:
                new_geo.setLeft(min(
                    new_geo.left() + delta.x(),
                    new_geo.right() - min_width
                ))
            if 'right' in self._resize_direction:
                new_geo.setRight(max(
                    new_geo.right() + delta.x(),
                    new_geo.left() + min_width
                ))
            if 'top' in self._resize_direction:
                new_geo.setTop(min(
                    new_geo.top() + delta.y(),
                    new_geo.bottom() - min_height
                ))
            if 'bottom' in self._resize_direction:
                new_geo.setBottom(max(
                    new_geo.bottom() + delta.y(),
                    new_geo.top() + min_height
                ))

            new_geo = new_geo.intersected(screen_rect)
            self.setGeometry(new_geo)

    def event(self, event):
        if event.type() == QMouseEvent.Type.MouseMove and not event.buttons():
            pos = event.position().toPoint()
            direction = self.get_resize_direction(pos)
            self.setCursor(self.get_resize_cursor(direction))
        return super().event(event)
    
    def get_resize_direction(self, pos):
        rect = self.rect()
        top = pos.y() <= self._resize_margin
        bottom = pos.y() >= rect.height() - self._resize_margin
        left = pos.x() <= self._resize_margin
        right = pos.x() >= rect.width() - self._resize_margin

        if left and top: return 'top-left'
        if left and bottom: return 'bottom-left'
        if right and top: return 'top-right'
        if right and bottom: return 'bottom-right'
        if left: return 'left'
        if right: return 'right'
        if top: return 'top'
        if bottom: return 'bottom'
        return None

    def get_resize_cursor(self, direction):
        if not direction: return QCursor(Qt.CursorShape.ArrowCursor)
        return {
            'left': Qt.CursorShape.SizeHorCursor,
            'right': Qt.CursorShape.SizeHorCursor,
            'top': Qt.CursorShape.SizeVerCursor,
            'bottom': Qt.CursorShape.SizeVerCursor,
            'top-left': Qt.CursorShape.SizeFDiagCursor,
            'bottom-right': Qt.CursorShape.SizeFDiagCursor,
            'top-right': Qt.CursorShape.SizeBDiagCursor,
            'bottom-left': Qt.CursorShape.SizeBDiagCursor
        }.get(direction, Qt.CursorShape.ArrowCursor)

    def mouseReleaseEvent(self, event):
        self.old_pos = None
        self._resize_direction = None
        self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
