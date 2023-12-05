import unittest

from tkinter_app import RsyncGUI
from unittest.mock import Mock, patch
from tkinter import Button, Tk


class TestRsyncGUI(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.gui = RsyncGUI(self.root)

    def test_copy(self):
        # copy_mock = Mock()
        # self.gui.copy_button.config()
        # self.gui.copy_button.invoke()
        # with patch.object(self.gui, self.gui.copy()) as mock_copy:
        #     root = Tk()
        #     copy_button = Button(root, text="Copy", command=self.gui.copy)
        #     copy_button.invoke()
        #     mock_copy.assert_called_once()
        #     root.destroy()
        copy_mock = Mock(wraps=self.gui.copy())
        self.gui.copy_button.config(command=copy_mock)
        self.gui.copy_button.invoke()
        copy_mock.assert_called_once()

