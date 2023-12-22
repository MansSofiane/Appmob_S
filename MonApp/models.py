from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=255)
    Prenom = models.CharField(max_length=255)
    Adresse_email = models.EmailField(unique=True)
    Mot_de_passe = models.CharField(max_length=255)
    Numero_de_telephone = models.CharField(max_length=15)
    Adresse_physique = models.TextField()
    Type_utilisateur = models.CharField(max_length=50)  # dépanneur, client, administrateur
    Is_Active = models.BooleanField(default=True)

class Depanneur(models.Model):
    MechanicID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Statut = models.CharField(max_length=100)
    Specialites = models.CharField(max_length=255)
    Position_geographique_latitude = models.FloatField()
    Position_geographique_longitude = models.FloatField()
    Evaluation_moyenne = models.FloatField()
    Types_vehicules_depannage = models.CharField(max_length=255)

class ServicesDeDepannage(models.Model):
    ServiceID = models.AutoField(primary_key=True)
    Nom_du_service = models.CharField(max_length=100)
    Description_du_service = models.TextField()
    Cout_du_service = models.DecimalField(max_digits=10, decimal_places=2)

class VehiculesDeDepannage(models.Model):
    TowTruckID = models.AutoField(primary_key=True)
    MechanicID = models.ForeignKey(Depanneur, on_delete=models.CASCADE)
    Modele_de_vehicule = models.CharField(max_length=100)
    Annee_de_fabrication = models.IntegerField()
    Plaque_dimmatriculation = models.CharField(max_length=20)
    Capacite_de_remorquage = models.FloatField()
    Statut = models.CharField(max_length=100)

class DemandesDeDepannage(models.Model):
    RequestID = models.AutoField(primary_key=True)
    Utilisateur_demandeur = models.ForeignKey(Users, on_delete=models.CASCADE)
    Type_de_service_demande = models.ForeignKey(ServicesDeDepannage, on_delete=models.CASCADE)
    Position_geographique_latitude = models.FloatField()
    Position_geographique_longitude = models.FloatField()
    Description_de_la_panne = models.TextField()
    Statut_de_la_demande = models.CharField(max_length=100)
    Depanneur_assigne = models.ForeignKey(Depanneur, on_delete=models.CASCADE, null=True, blank=True)
    Vehicule_de_depannage_assigne = models.ForeignKey(VehiculesDeDepannage, on_delete=models.CASCADE, null=True, blank=True)
    Date_et_heure_de_la_demande = models.DateTimeField(auto_now_add=True)

class HistoriqueDesDepannages(models.Model):
    HistoryID = models.AutoField(primary_key=True)
    Depanneur_associe = models.ForeignKey(Depanneur, on_delete=models.CASCADE)
    Utilisateur_associe = models.ForeignKey(Users, on_delete=models.CASCADE)
    Type_de_service_fourni = models.ForeignKey(ServicesDeDepannage, on_delete=models.CASCADE)
    Vehicule_de_depannage_utilise = models.ForeignKey(VehiculesDeDepannage, on_delete=models.CASCADE)
    Position_geographique_latitude = models.FloatField()
    Position_geographique_longitude = models.FloatField()
    Description_de_la_panne = models.TextField()
    Cout_du_depannage = models.DecimalField(max_digits=10, decimal_places=2)
    Date_et_heure_du_depannage = models.DateTimeField(auto_now_add=True)
    Statut_du_depannage = models.CharField(max_length=100)

class AvisEtEvaluations(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    Depanneur_evalue = models.ForeignKey(Depanneur, on_delete=models.CASCADE)
    Utilisateur_evaluateur = models.ForeignKey(Users, on_delete=models.CASCADE)
    Note = models.FloatField()
    Commentaire = models.TextField()
    Date_de_lavis = models.DateTimeField(auto_now_add=True)

class Paiements(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    Utilisateur_associe = models.ForeignKey(Users, on_delete=models.CASCADE)
    Montant = models.DecimalField(max_digits=10, decimal_places=2)
    Date_et_heure_de_la_transaction = models.DateTimeField(auto_now_add=True)
    Statut = models.CharField(max_length=100)

class Notifications(models.Model):
    NotificationID = models.AutoField(primary_key=True)
    Destinataire = models.CharField(max_length=100)  # Remplacez par le type approprié (MechanicID, UserID, etc.)
    Contenu_de_la_notification = models.TextField()
    Date_et_heure_denvoi = models.DateTimeField(auto_now_add=True)
    Statut = models.CharField(max_length=100)

class Tarifs(models.Model):
    PricingID = models.AutoField(primary_key=True)
    ServiceID = models.ForeignKey(ServicesDeDepannage, on_delete=models.CASCADE)
    MechanicID = models.ForeignKey(Depanneur, on_delete=models.CASCADE)
    Cout = models.DecimalField(max_digits=10, decimal_places=2)
    Is_active = models.BooleanField(default=True)