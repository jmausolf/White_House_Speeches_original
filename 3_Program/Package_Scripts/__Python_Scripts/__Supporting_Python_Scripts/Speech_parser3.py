def WHT3(url):
    """Prints Text Output for a given URL from Whitehouse Speeches and Remarks"""
    
    import urllib2,sys, random
    import os
    from bs4 import BeautifulSoup


    soup = BeautifulSoup(urllib2.urlopen(url).read())

    # Get URL
    url2 = "Cite: \n"+url+"\n"
    
    try:
        # Get Paragraph Body2
        content2 = soup.find("div", {"class":"legacy-content"})
        paragraph2 = ["".join(x.findAll(text=True)) for x in content2.findAll("div")]
        paragraph_body2 = "\n\n%s" % ("\n\n".join(paragraph2))

        # Get Paragraph Body1
        content1 = soup.find("div", {"id":"content"})
        paragraph1 = ["".join(x.findAll(text=True)) for x in content1.findAll("p")]
        paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1))

        str_id = url[60:75]
        date_id = "2009-2010"+'-'+str(date2)+str_id


    except:
        # Get Paragraph Body1
        content1 = soup.find("div", {"id":"content"})
        paragraph1 = ["".join(x.findAll(text=True)) for x in content1.findAll("p")]
        paragraph_body1 = "\n\n%s" % ("\n\n".join(paragraph1))


        str_id = url[60:75]
        date_id = "2009-2010"+'-'+str_id


    #Random ID
    randID1 = str(random.randrange(6, 10000, 1))
    randID2 = str(random.randrange(6, 10000, 1))

    try:
        path1 = date_id+"_"+"ID1"+".txt"
        path2 = date_id+"_"+"ID2"+".txt"
        path3 = date_id+"_"+"ID3"+".txt"
        path4 = date_id+"_"+"ID4"+".txt"
        path5 = date_id+"_"+"ID5"+".txt"
        if os.path.isfile(path1) == False:
            #print "no file ID1 found, create ID1"
            f = open(date_id+"_"+"ID1"+".txt", 'w')
            f.write(url2.encode('utf-8'))
            f.write(paragraph_body1.encode('utf-8'))
            f.write(paragraph_body2.encode('utf-8'))
            f.close
            return

        elif os.path.isfile(path1) == True:
            #print "found file ID1, check for ID2"
            if os.path.isfile(path2) == False:
                print "found ID1, no file ID2 found, make ID2"
                f = open(date_id+"_"+"ID2"+".txt", 'w')
                f.write(url2.encode('utf-8'))
                f.write(paragraph_body1.encode('utf-8'))
                f.write(paragraph_body2.encode('utf-8'))
                f.close
                return
            elif os.path.isfile(path2) == True:
                #print "found file ID2, check for ID3"
                if os.path.isfile(path3) == False:
                    print "found IDs 1-2, no file ID3 found, make ID3"
                    f = open(date_id+"_"+"ID3"+".txt", 'w')
                    f.write(url2.encode('utf-8'))
                    f.write(paragraph_body1.encode('utf-8'))
                    f.write(paragraph_body2.encode('utf-8'))
                    f.close
                    return
                elif os.path.isfile(path3) == True:
                    #print "found file ID3, check for ID4"
                    if os.path.isfile(path4) == False:
                        print "found IDs 1-3, no file ID4 found, make ID4"
                        f = open(date_id+"_"+"ID4"+".txt", 'w')
                        f.write(url2.encode('utf-8'))
                        f.write(paragraph_body1.encode('utf-8'))
                        f.write(paragraph_body2.encode('utf-8'))
                        f.close
                        return
                    elif os.path.isfile(path4) == True:
                        #print "found file ID4, check for ID5"
                        if os.path.isfile(path5) == False:
                            print "found IDs 1-4, no file ID5 found, make ID5"
                            f = open(date_id+"_"+"ID5"+".txt", 'w')
                            f.write(url2.encode('utf-8'))
                            f.write(paragraph_body1.encode('utf-8'))
                            f.write(paragraph_body2.encode('utf-8'))
                            f.close
                            return
                        elif os.path.isfile(path5) == True:
                            print "found IDs 1-5, create random ID"
                            f = open(date_id+"_"+"ID"+randID1+"-"+randID2+".txt", 'w')
                            f.write(url2.encode('utf-8'))
                            f.write(paragraph_body1.encode('utf-8'))
                            f.write(paragraph_body2.encode('utf-8'))
                            f.close
                            return 

        
    finally:
        pass




#Test
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-qa-session-closing-fiscal-responsibility-summit-2-23-09"
#url = "http://www.whitehouse.gov/the-press-office/remarks-president-senate-passage-health-insurance-reform"
#url = "http://www.whitehouse.gov/the-press-office/press-availability-president-obama-and-prime-minister-rudd-australia"
#WHT3(url)