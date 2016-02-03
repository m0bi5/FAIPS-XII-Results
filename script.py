from selenium import webdriver
from prettytable import PrettyTable

browser=webdriver.PhantomJS(executable_path="C:\\Users\\Bhasi\\Desktop\\Sonus Files\\phantomjs.exe")

file =open('results.txt','w')
def getMarks(roll):
    browser.get("http://cbseresults.nic.in/class12/cbse122015_all.htm")
    browser.find_element_by_tag_name("input").send_keys(roll)
    browser.find_element_by_name("B1").click()
    name= browser.find_elements_by_tag_name("td")[10].text
    le= len(browser.find_elements_by_xpath("//table[@width='75%']/tbody/tr"))+1
    li=[]
    tpain=le-10
    subs=[]
    for x in range (0,tpain):
        m1=browser.find_elements_by_tag_name("td")[25+((x)*6)].text
        m1=m1.split(' ')
        m2=browser.find_elements_by_tag_name("td")[22+((x)*6)].text
        m2=m2.split(' ')
        subs.append(m2[0])
        if m1[0]=='---':
            li.append(browser.find_elements_by_tag_name("td")[(25+((x)*6))+1].text)
        elif m1[0]=='':
            li.append('0')
        else:
            li.append(m1[0])
    m=[]
    for item in li:
        if item[0]=='0' or item[0]=='1' or item[0]=='2' or item[0]=='3' or item[0]=='4' or item[0]=='5' or item[0]=='6' or item[0]=='7' or item[0]=='8' or item[0]=='9':
            m.append(item)
    m=list(map(int,m))
    ns=le-10
    marks=sum(m)/ns
    results=[]
    results.append(name)
    for x in range(0,ns):
        results.append(subs[x])
        results.append(li[x])
    results.append(marks)
    tab=PrettyTable([x for x in subs])
    tab.add_row([y for y in li])
    tab.add_column('PERCENTAGE',[marks])
    tab='\n\n'+name+'\n'+str(tab)

    return tab


start=9103835
stop=9103999
while start<=stop:
    print (start)
    with open('results.txt', 'a') as the_file:
        the_file.write(getMarks(str(start)))
    start+=1
