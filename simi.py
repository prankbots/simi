# -*- coding: utf-8 -*-

import PRANKBOTS
from PRANKBOTS.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, re, os, ast, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, tempfile, glob, shutil, unicodedata

cl = PRANKBOTS.LINE()
cl.login(token="")
cl.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

KAC=[cl]
mid = cl.getProfile().mid
Bots=[mid,"ufce863f62f40706c01fa4a3c3c4cb096"]
admin=["ufce863f62f40706c01fa4a3c3c4cb096"]

wait = {
    'contact':False,
    'timeline':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":30},
    #'leaveRoom':True,
    'autoAdd':True,
    'message':"""THANKS FOR ADD ME\n\nSUBCRABE ME ON YOUTUBE\n\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ""",
    "lang":"JP",
    "comment1":"❂•••••••••••••••••••••••••❂\n                  https://line.me/R/ti/p/%40eiya4481p\n『⊰์◉⊱ᎢᎬᎪᎷ ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』",
    "likeOn":True,
    "alwaysRead":True,
    "simiSimi":True,
}
settings = {
    "simiSimi":{}
    }
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True: 
                cl.findAndAddContactsByMid(op.param1)
                xname = cl.getContact(op.param1).displayName
                cl.sendText(op.param1, "Halo " + xname + "THANKS FOR ADD ME\n\nSUBCRABE ME ON YOUTUBE\n\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
#--------------------------------------------------------
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        cl.rejectGroupInvitation(op.param1)
		    else:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			cl.updateGroup(G)
			Ti = cl.reissueGroupTicket(op.param1)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
			cl.sendText(op.param1,"THANKS TO INVITE YOUTUBE SUBCRABE\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
                else:
		    if op.param2 in admin:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			cl.updateGroup(G)
			Ti = cl.reissueGroupTicket(op.param1)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
			cl.sendText(op.param1,"DI SUBCRABE KAK\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
		    else:
                        cl.rejectGroupInvitation(op.param1)

        if op.type == 13:
            cl.acceptGroupInvitation(op.param1) 
            xname = cl.getContact(op.param2).displayName
            cl.sendText(op.param1,"Thanks" + "@"+xname+ "\nYUK SUBCRABE CHANNEL NYA KLIK LINK NYA\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ" + datetime.today().strftime('\n───────────\n⏰(%H:%M:%S)'))
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':'ufce863f62f40706c01fa4a3c3c4cb096'}
            cl.sendMessage(c)

#        if op.type == 22:
 #           if wait["leaveRoom"] == True:
  #              cl.leaveRoom(op.param1)
   #     if op.type == 24:
    #        if wait["leaveRoom"] == True:
     #           cl.leaveRoom(op.param1)
      #      if msg.toType == 1:
       #         if wait["leaveRoom"] == True:
        #            cl.leaveRoom(msg.to)
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
            cl.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
            cl.leaveRoom(op.param1)

#            if msg.contentType == 16:
 #               url = msg.contentMetadata["postEndUrl"]
  #              cl.like(url[25:58], url[66:], likeType=1001)
   #             cl.comment(url[25:58], url[66:], wait["comment1"])
#        if op.type == 26:
 #           msg = op.message
  #          if wait["alwaysRead"] == True:
   #             if msg.toType == 0:
    #                cl.sendChatChecked(msg.from_,msg.id)
     #           else:
      #cl.sendChatChecked(msg.to,msg.id)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to,data['result']['response'].encode('utf-8'))
        if op.type == 26:
            msg = op.message

#----------------------------------------------------------------------------


            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     cl.like(url[25:58], url[66:], likeType=1005)
                     cl.comment(url[25:58], url[66:], wait["comment1"])
                     cl.sendText(msg.to,"Aku sudah like kakak :D")
            elif msg.text is None:
                return
            elif msg.text in ["Simi","Simi:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"BOT API SIMISIMI TURN ON")
                cl.sendText(msg.to,"CREATOR ON SUBCRABE\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
                
            elif msg.text in ["Simi:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"BOT API SIMISIMI TURN OFF")
                cl.sendText(msg.to,"CREATOR ON SUBCRABE\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
            elif "Simi@bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"BYE BYE KAKAK JANGAN LUPA SUBCRABE CHANNEL NYA..\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leavegroup"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                for i in gid:
                  cl.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh selfbot...!!!\nMakasih...!!!")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
        if op.type == 59:
            print op


    except Exception as error:
        print error
                
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
