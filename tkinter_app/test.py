# import unittest
#
# import time
# from tkinter_app import RsyncGUI
# from unittest.mock import Mock, patch
from tkinter import Button, Tk


import unittest
from unittest import mock

from tkinter_app import RsyncGUI


class RsyncGUITest(unittest.TestCase):

	def setUp(self):
		self.root = Tk()
		with mock.patch('tkinter.Tk'):
			self.rs = RsyncGUI(self.root)

	def test_browse_source(self):
		self.rs.browse_source()
		self.assertEqual(self.rs.source_entry.get(), "")

	def test_browse_dest(self):
		self.rs.browse_dest()
		self.assertEqual(self.rs.dest_entry.get(), "")

	def test_copy_empty_fields(self):
		self.rs.copy()
		self.assertEqual(self.rs.show_error_copy_called, True)

	# def test_copy_success(self):
	# self.rs.source_entry.insert(0, "D:/OneDrive/Рабочий стол/Фото")
	# self.rs.dest_entry.insert(0, "D:/Учеба")
	# self.rs.copy()
	# self.assertEqual(self.rs.show_error_copy_called, False)
	# self.assertEqual(self.rs.success_info_called, True)

	# def test_setting_server_save(self):
	# self.rs.ip_entry.insert(0, "127.0.0.1")
	# self.rs.save_user_data()
	# # test your expected behavior when saving user data, such as updating attributes or checking results
