from test_TP05z import *

##################################
## Proc�dure d'ex�cution des tests
##################################

DICO = {'01_lecteur_fou': LecteurFouTest,
    		'02_prison_sikinia': PrisonSikiniaTest,
    		'03_rentree': RentreeTest,
    		'04_foret_rapide': ForetRapideTest,
    		'05_foret_long': ForetLongTest,
    		'06_foret_tres_long': ForetTresLongTest,
    		'07_petits_pois_rapide': PetitsPoisCourtsTest,
    		'08_petits_pois_moyen': PetitsPoisMoyenTest,
    		'09_petits_pois_long': PetitsPoisLongTest,
    		'10_petits_pois_tres_long': PetitsPoisTresLongTest,
            }

def fais_tests(choix):
    '''Fonction qui appelle les batteries de test selon le choix de
    l'utilisateur.'''
    try:
        suite = unittest.TestLoader().loadTestsFromTestCase(DICO[choix])
    except:
        print('='*70)
        print('Le choix "%s" ne fait pas partie des possibilites suivantes:' % choix)
        s = '\n  * '
        print(s[1:] + s.join(sorted(list(DICO.keys()))))
        print('='*70)
        exit()
    unittest.TextTestRunner(verbosity=2).run(suite)


def calcule_note():
    '''Fonction qui calcule automatiquement la note de l'�l�ve au prorata du
    nombre de tests pass�s avec succ�s.'''
    liste_testcases = ['test_TP05.' + elem.__name__ for elem in DICO.values()]
    suite = unittest.TestLoader().loadTestsFromNames(liste_testcases)
    f = open('erreurs.txt','w')
    res = unittest.TextTestRunner(stream=f,verbosity=1).run(suite)
    f.close()
    f = open('erreurs.txt','r')
    explications = '''Resultats des tests: E = Error, F = Failure, . = Success'''
    s_ex = '\n' + '*'*len(explications) + '\n' + explications + '\n' + '*'*len(explications)
    print(s_ex)
    print(f.readline())
    f.close()
    total = res.testsRun
    failed= len(res.failures)
    errors= len(res.errors)
    success = total - failed - errors
    print("Vous avez reussi {} tests sur un total de {}.".format(success,total))
    print("Note indicative: {}/20 (sans compter la penalite 'commentaires')".format(int(success/total*20)))

def detaille_note():
    '''Pour calculer les notes � chaque sous-suite de tests.'''
    total_general  = 0
    success_general= 0
    for k in sorted(DICO.keys()):
        s = unittest.TestLoader().loadTestsFromTestCase(DICO[k])
        f = open('erreurs.txt','w')
        res = unittest.TextTestRunner(stream=f,verbosity=1).run(s)
        f.close()
        total = res.testsRun
        failed= len(res.failures)
        errors= len(res.errors)
        success = total - failed - errors
        print("{}/{}".format(success,total),k)
        total_general += total
        success_general += success
    print('='*20)
    print('Globalement: {}/{}'.format(success_general,total_general))
    return 'Note indicative: {}/20'.format(round(success_general/total_general*20,2))
