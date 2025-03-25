# Start of a package that implements morphology in general
# -*- coding: utf-8 -*-

import comline

import json
import logging
import os
import webapp2

from google.appengine.ext.webapp import template

from morphologizer import Morphologizer
import morph_fr

from langmodel import LangModel, Verb
from morph_fr import MorphFr
from morph_fr import FrenchLang

class MainHandler(webapp2.RequestHandler):
    def get(self):
        morpher = Morphologizer()
        template_values = {
          'lang_list': morpher.lang_codes
        }
        path = os.path.join(os.path.dirname(__file__), 'morphologizer_main.html')
        self.response.out.write(template.render(path, template_values))


class SelectLang(webapp2.RequestHandler):
    def get(self):
        # Get the language parameter
        lang_code = self.request.get('lang_code', allow_multiple=False)
        # Instantiate the class for the language
        lang_model = LangModel(lang_code)
        lang_name = 'unspecified'
        try:
            lang_name = lang_mode.lang_name
        except:
            pass

        if lang_code == 'fr':
            morpher = MorphFr()
            
        if lang_model:
            # Get the verb info
            # put into the template
            template_values = {
                'lang_code': lang_code,
                'lang_name': lang_name,
            }
            path = os.path.join(os.path.dirname(__file__), 'morphologizer_lang.html')
            self.response.out.write(template.render(path, template_values))
        else:
            template_values = {
                'lang_code': lang_code,
            }
            path = os.path.join(os.path.dirname(__file__), 'morphologizer_unsupported.html')
            self.response.out.write(template.render(path, template_values))



class GetVerbHandler(webapp2.RequestHandler):
    # Given a language and a verb, get its morphology

    def get(self):
        # Get parameters
        logging.info('GetVerHandler')

        lang_code = self.request.get('lang_code', 'und')
        verb_in = self.request.get('verb', 'le dessin')

        logging.info('GetVerbHandler: %s, %s', lang_code, verb_in)
                     
        if lang_code == 'fr':
            morpher = MorphFr()
            
            frenchLangModel = FrenchLang()
            morph = morph_fr.MorphFr(frenchLangModel)
            morph_fr.setupBasicFrench(frenchLangModel)
            v = morph_fr.FrenchVerb(frenchLangModel, verb_in)

            conjugation = v.get_conjugation_table()    

        # TODO: Compute the result
        morph_out = {
            'message': 'TBD',
            'conjugation': conjugation,
        }
        result = {'lang_code': lang_code,
                  'verb_in': verb_in,
                  'morph_out': morph_out
                  }
        self.response.out.write(json.dumps(result))
    

app = webapp2.WSGIApplication(
    [
        ('/', MainHandler),
        ('/select/', SelectLang),
        ('/get_verb/', GetVerbHandler),
    ],
    debug=True)

#app.error_handlers[404] = handle_404
#app.error_handlers[500] = handle_500
        
