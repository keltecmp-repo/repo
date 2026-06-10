# -*- coding: utf-8 -*-
# KeltecPinGuard - MPAA Lookup module
# Updated for Python 3 / Kodi 19+ (Matrix, Nexus, Omega)

import json
import traceback
import urllib.request
import urllib.parse

from resources.lib.settings import log


class MpaaLookup():
    def __init__(self):
        self.imdb_url_prefix = 'http://www.omdbapi.com/'

    def getMpaaRatings(self, name, year=''):
        mpaa = None
        if year not in [None, "", "0"]:
            mpaa = self.getIMDB_mpaa_by_name(name, str(year), True)
        if mpaa in [None, ""]:
            mpaa = self.getIMDB_mpaa_by_name(name, '', True)
        if (mpaa in [None, ""]) and (year not in [None, "", "0"]):
            mpaa = self.getIMDB_mpaa_by_name(name, str(year), False)
        if mpaa in [None, ""]:
            mpaa = self.getIMDB_mpaa_by_name(name, '', False)
        return mpaa

    def getIMDB_mpaa_by_name(self, name, year='', isTvShow=True):
        log("IdLookup: Getting IMDB Mpaa by name %s, year=%s, tv=%s" % (name, year, str(isTvShow)))
        clean_name = urllib.parse.quote(name)
        query = '?t=%s' % clean_name
        if year not in [None, '', '0']:
            query = '%s&y=%s' % (query, str(year))
        if isTvShow:
            query = '%s&type=series' % query
        else:
            query = '%s&type=movie' % query
        url = "%s%s" % (self.imdb_url_prefix, query)
        log("MpaaLookup: Using call: %s" % url)
        json_details = self._makeCall(url)
        mpaa = None
        if json_details not in [None, ""]:
            json_response = json.loads(json_details)
            if json_response.get('Response', 'False') == 'True':
                if 'Rated' in json_response:
                    mpaa = json_response.get('Rated', None)
                    if mpaa not in [None, ""]:
                        mpaa = str(mpaa)
                        log("MovieLookup: Found mpaa %s" % str(mpaa))
                        if mpaa in ["N/A"]:
                            mpaa = None
            else:
                log("MpaaLookup: No results returned for imdb mpaa search")
        return mpaa

    def _makeCall(self, url):
        log("MpaaLookup: Making query using %s" % url)
        resp_details = None
        try:
            req = urllib.request.Request(url)
            req.add_header('Accept', 'application/json')
            response = urllib.request.urlopen(req)
            resp_details = response.read().decode('utf-8')
            try:
                response.close()
                log("MpaaLookup: Request returned %s" % resp_details)
            except Exception:
                pass
        except Exception:
            log("MpaaLookup: Failed to retrieve details from %s: %s" % (url, traceback.format_exc()))
        return resp_details
