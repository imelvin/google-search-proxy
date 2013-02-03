import urllib2,urllib
import simplejson    
import sys

def google_search(searchstr, page, rsz):
    results = []

    page = (page-1) * rsz
    if page < 0:
        page = 0

    #print chardet.detect(searchstr)
    #print urllib.quote(searchstr.encode('utf8'))
    url = ('http://ajax.googleapis.com/ajax/services/search/web'
                  '?v=1.0&q=%s&rsz=%s&start=%s&hl=zh-CN') % (urllib.quote(searchstr.encode('utf8')), rsz, page)
    #print url
    try:
        request = urllib2.Request(
        url, None, {'Referer': 'http://www.sina.com'})
        response = urllib2.urlopen(request)

    # Process the JSON string.
        rs = simplejson.load(response)
        infoaaa = rs['responseData']['results']
        results = infoaaa
    except Exception,e:
        print e
    else:
        for minfo in infoaaa:
            print minfo['url']
        print '---------------------'
    return results

def main():
    s = raw_input('search:')
    
    results = google_search(s, 1, 8)
    print len(results)
    for r in results:
        print r['url']
        print r['titleNoFormatting']
        print r['title']
        print r['content']
        print '---'

if __name__ == "__main__":
    main()
