# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, re, os, ast, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, tempfile, glob, shutil, unicodedata

prank = LINETCR.LINE()
prank.login(token="Eps6viYeGUDD0GdVgDV6.9zkQQXcYKYEwrakH49bR5G.SI2heZoRS+kDt3XjmJzI0DMTVkQxn5INNCPGqzSl84I=")
prank.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

KAC=[cl]
mid = prank.getProfile().mid
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
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
settings = {
    "simiSimi":{}
    }
setTimesetTime = {}
setTime = wait2['setTime']
mulai = time.time() 
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True: 
                prank.findAndAddContactsByMid(op.param1)
                xname = prank.getContact(op.param1).displayName
                prank.sendText(op.param1, "Halo " + xname + "THANKS FOR ADD ME\n\nSUBCRABE ME ON YOUTUBE\n\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
#--------------------------------------------------------
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = prank.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        prank.rejectGroupInvitation(op.param1)
		    else:
                        prank.acceptGroupInvitation(op.param1)
			G = prank.getGroup(op.param1)
			G.preventJoinByTicket = False
			prank.updateGroup(G)
			Ti = prank.reissueGroupTicket(op.param1)
			G.preventJoinByTicket = True
			prank.updateGroup(G)
			prank.sendText(op.param1,"THANKS TO INVITE YOUTUBE SUBCRABE\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
                else:
		    if op.param2 in admin:
                        prank.acceptGroupInvitation(op.param1)
			G = prank.getGroup(op.param1)
			G.preventJoinByTicket = False
			prank.updateGroup(G)
			Ti = prank.reissueGroupTicket(op.param1)
			G.preventJoinByTicket = True
			prank.updateGroup(G)
			prank.sendText(op.param1,"DI SUBCRABE KAK\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
		    else:
                        prank.rejectGroupInvitation(op.param1)

        if op.type == 13:
            prank.acceptGroupInvitation(op.param1) 
            xname = prank.getContact(op.param2).displayName
            prank.sendText(op.param1,"Thanks" + "@"+xname+ "\nYUK SUBCRABE CHANNEL NYA KLIK LINK NYA\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ" + datetime.today().strftime('\n───────────\n⏰(%H:%M:%S)'))
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':'ufce863f62f40706c01fa4a3c3c4cb096'}
            prank.sendMessage(c)
	    if msg.contentMetadata != {}:
                try:
                    prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                    tagme = False
                    for i in range(len(prov)):
                        if prov[i]["M"] == mid:
                            tagme = True
                            break
                    if tagme:
                        msg.contentType = 7
                        msg.text = ''
                        msg.contentMetadata = {
                                                  'STKPKGID': '1',
                                                  'STKTXT': '[]',
                                                  'STKVER': '100',
                                                  'STKID':'10'
                                              }
                        prank.sendText(msg.to,"ada apa kak hehe")
                        prank.sendMessage(msg)
                except:
                    pass
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
            prank.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
            prank.leaveRoom(op.param1)
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
                                prank.sendText(msg.to,data['result']['response'].encode('utf-8'))
        if op.type == 26:
            msg = op.message

#----------------------------------------------------------------------------
            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    prank.sendChatChecked(msg.from_,msg.id)
                else:
                    prank.sendChatChecked(msg.to,msg.id)
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     prank.like(url[25:58], url[66:], likeType=1005)
                     prank.comment(url[25:58], url[66:], wait["comment1"])
                     prank.sendText(msg.to,"Aku sudah like kakak :D")
            elif msg.text is None:
                return
            elif msg.text in ["Simi","Simi:on"]:
                settings["simiSimi"][msg.to] = True
                prank.sendText(msg.to,"BOT API SIMISIMI TURN ON")
                prank.sendText(msg.to,"CREATOR ON SUBCRABE\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
                
            elif msg.text in ["Simi:off"]:
                settings["simiSimi"][msg.to] = False
                prank.sendText(msg.to,"BOT API SIMISIMI TURN OFF")
                prank.sendText(msg.to,"CREATOR ON SUBCRABE\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
            elif "Simi@bye" in msg.text:
                if msg.toType == 2:
                    ginfo = prank.getGroup(msg.to)
                    try:
                        prank.sendText(msg.to,"BYE BYE KAKAK JANGAN LUPA SUBCRABE CHANNEL NYA..\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
                        prank.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Leavegroup"]: 
              if msg.from_ in admin:
                gid = prank.getGroupIdsJoined()
                for i in gid:
                  prank.leaveGroup(i)
                if wait["lang"] == "JP":
                  prank.sendText(msg.to,"Untuk group " + str(ginfo.name) + "\nBYE BYE KAKAK JANGAN LUPA SUBCRABE CHANNEL NYA..\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
                else:
                  prank.sendText(msg.to,"He declined all invitations")
            elif "Simi@tagall" in msg.text:
                group = prank.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*500 : (j+1)*500]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    prank.sendMessage(msg) 
                    prank.sendText(msg.to,"HAY KAMU SUBCRABE YUK CHANNEL TEMEN SIMI. 😄\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
            elif "Simi@cctv" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     print wait2
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             prank.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = prank.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          prank.sendMessage(msg)
                          prank.sendText(msg.to,"HAY KANG NGINTIP JANGAN LUPA SUBCRABE CHANNEL NYA.. 😂\nhttps://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ")
                        except Exception as error:
                              print error
                        pass
               
                    else:
                        prank.sendText(msg.to, "Lurking has not been set.")
            elif msg.text in ["Simi@grup"]:
                 gid = prank.getGroupIdsJoined()
                 h = ""
                 for i in gid:
                  h += "[⛓️] %s \n" % (prank.getGroup(i).name + " | 🗜️Members : " + str(len (prank.getGroup(i).members)))
                 prank.sendText(msg.to, "☆「Group List simsimi kak ini」☆\n"+ h +"🗜️Total Group : " +str(len(gid)))
            elif msg.text in ["Simi@me"]:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': msg.from_}
                        cl.sendMessage(msg)
                        cl.sendText(msg.to,"ini yah kontak kakak .. jelek amat kak kayak badut 😂")
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
                       
        if op.type == 59:
            print op


    except Exception as error:
        print error
                
while True:
    try:
        Ops = prank.fetchOps(prank.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(prank.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            prank.Poll.rev = max(prank.Poll.rev, Op.revision)
            bot(Op)