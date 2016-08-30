intrest#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
#print("I know that these are the words the user typed on the command line: ", argv)

def alphabet_position(letter):
	letter = letter.lower()
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	return alphabet.index(letter)

def rotate_character(char, rot):
	if char.islower():
		alphabet = "abcdefghijklmnopqrstuvwxyz"
	else:
		alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	rotated_index = alphabet_position(char) + int(rot)
	rotated = alphabet[rotated_index % 26]
	return rotated

def encrypt(text, rot):
	encrypt = ""
	for char in text:
		if char.isalpha() == False:
			encrypt = encrypt + char
		else:
			encrypt = encrypt + rotate_character(char, rot)
	return encrypt

# write my variable form
form="""
<!DOCTYPE html>
<html>
<head>
<form method="post">
    <input name="text">
    <input name="rot">
    <input type="submit">
</form>
<head>
<html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
        text = self.request.get("text")
        rot = self.request.get("rot")
        response = encrypt(text, int(rot))
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
