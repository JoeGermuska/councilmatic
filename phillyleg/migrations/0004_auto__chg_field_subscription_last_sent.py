# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Subscription.last_sent'
        db.alter_column('phillyleg_subscription', 'last_sent', self.gf('django.db.models.fields.DateTimeField')())


    def backwards(self, orm):
        
        # Changing field 'Subscription.last_sent'
        db.alter_column('phillyleg_subscription', 'last_sent', self.gf('django.db.models.fields.DateField')())


    models = {
        'phillyleg.councilmember': {
            'Meta': {'object_name': 'CouncilMember'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'phillyleg.councilmembersubscription': {
            'Meta': {'object_name': 'CouncilMemberSubscription'},
            'councilmember': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['phillyleg.CouncilMember']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subscription': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'councilmembers'", 'to': "orm['phillyleg.Subscription']"})
        },
        'phillyleg.keywordsubscription': {
            'Meta': {'object_name': 'KeywordSubscription'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subscription': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'keywords'", 'to': "orm['phillyleg.Subscription']"})
        },
        'phillyleg.legaction': {
            'Meta': {'unique_together': "(('file', 'date_taken', 'description', 'notes'),)", 'object_name': 'LegAction'},
            'acting_body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'date_taken': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['phillyleg.LegFile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'motion': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'notes': ('django.db.models.fields.TextField', [], {})
        },
        'phillyleg.legfile': {
            'Meta': {'object_name': 'LegFile'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'controlling_body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'date_scraped': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'final_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'intro_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'key': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'last_scraped': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sponsors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['phillyleg.CouncilMember']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'phillyleg.legfileattachment': {
            'Meta': {'unique_together': "(('file', 'url'),)", 'object_name': 'LegFileAttachment'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['phillyleg.LegFile']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'phillyleg.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_sent': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['phillyleg']
