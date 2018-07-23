#! /usr/bin/python
# -*- coding: utf-8 -*-

import telebot, os
from telebot import types
import random, telebot.apihelper

import thread
from time import sleep
import json
import datetime
import smtplib
import requests

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '699240238:AAEAObA6JI-gxZbRwf8XM2pgNHN2bFAkwbM'

class ByeByeBot(object):

	def __init__(self, TOKEN):
		
		self.bot = telebot.TeleBot(TOKEN)
		self.run()

	def run(self):

		try:
			self.bot.set_update_listener(self.__listener)
			self.bot.polling()

		except requests.exceptions.ReadTimeout:
			print("ReadTimeOutError")

	def __listener(self, msgs):

		if self.id_message_kicked != None:

			self.bot.delete_message(self.chat_id_message_kicked, self.id_message_kicked+1)
			self.id_message_kicked = None

		for m in msgs:

			print(m)

			# Check if is a new member
			if m.new_chat_member != None:

				try:
					first_name = m.new_chat_member.first_name
				except:
					first_name = ""

				try:
					username = m.new_chat_member.username
				except:
					username = ""

				if len(first_name) > 15 or len(username) > 15 or 1:

					# Try kick user (not a user rly, is a fucking bot)
					self.bot.kick_chat_member(m.chat.id, m.new_chat_member.id)

					# Delete the message
					self.bot.delete_message(m.chat.id, m.message_id)
					self.bot.delete_message(m.chat.id, m.message_id+1)

if __name__ == '__main__':

	bot = ByeByeBot(TOKEN)