from django.db import models

class Produit(models.Model):
    nom_article = models.CharField(max_length=100, blank=False)
    quantite = models.IntegerField(blank=False)
    prix = models.FloatField(blank=False)
    date_peremption = models.DateTimeField()
    Numero_lot = models.IntegerField()

    class Meta:
        abstract = True

    
    def __str__(self):
        return "nom: {0} Prix: {1} Quantité: {2}".format(self.nom_article, self.prix, self.quantite)

class Petit_matériel(Produit):
    pass 

class Parapharmatie(Produit):
    pass 

class Dietetique(Produit):
    pass 

class Article(models.Model):
    choix_groupe = (
        ('liste 1', 'Produit toxique'),
        ('Liste 2', 'Produit dangereux'),
        ('Stupéfiant', 'Stupéfiants'),
    )
    groupe = models.CharField(max_length=20, choices=choix_groupe, blank=True)
    dci = models.CharField(max_length=100, blank=True)
    specialite = models.CharField(max_length=100, blank=False)
    dose = models.CharField(max_length=100, blank=False, default='500 mg')
    quantite = models.IntegerField(blank=False)
    classe_therapeutic = models.TextField(blank=True)
    prix = models.FloatField(blank=False)
    choix_presentation = (
        ('SUPPO & OVULE', 'Suppositoire et ovule'),
        ('GOUTTE NASALE', 'Goutte nasale'),
        ('GOUTTE NASALE', 'Goutte nasale'),
        ('AMPOULE BUVABLE', 'Ampoule buvable'), 
        ('SACHET', 'Sachets'),
        ('SOLUTE', 'Solute'),
        ('COMPRIMÉ', 'Comprimé'),
        ('SIROP', 'Sirop'),
        ('POUDRE', 'Poudre'),
    )
    presentation = models.CharField(max_length=20, choices=choix_presentation, blank=True)
    date_peremption = models.DateTimeField()
    Numero_lot = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return  "Spécialité: {0} Dci: {1} prix: {2} quantité: {3}".format(
            self.specialite, self.dci, self.prix, self.quantite
        )

class Medicament(Article): 
    pass 
