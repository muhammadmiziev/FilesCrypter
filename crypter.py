#!/usr/bin/env python3
# -*- coding utf-8 -*-

import os, json, AESCrypter


with open('./config.json') as data_file:
    CONFIG = json.load(data_file)



class Encrypt():

    # configs
    KEY = CONFIG['KEY']
    path = CONFIG['TARGET_PATH']

    listfiles = os.listdir(path)

    def __init__(self):
        files = self.generateListFiles()
        self.cryptFiles(files);

    def generateListFiles(self):
        files = []
        for f in self.listfiles:
            files.append(self.path+f)
        return files

    def cryptFiles(self, files):
        aes = AESCrypter.Init(self.KEY.encode('utf-8'));
        for f in files:
            res = self.getFileContent(f)
            crypt = aes.encrypt(res)
            self.writeToFile(f, crypt)

    def getFileContent(self, file):
        f = open(file, 'rb')
        result = f.read();
        f.close();

        return result;

    def writeToFile(self, file, data):
        f = open(file, 'wb')
        result = f.write(data);
        f.close();

        return 1;

Encrypt();
