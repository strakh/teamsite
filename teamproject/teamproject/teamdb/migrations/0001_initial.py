# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employee'
        db.create_table('teamdb_employee', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state_province', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('specialization', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('education', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('skils', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=600)),
        ))
        db.send_create_signal('teamdb', ['Employee'])

        # Adding model 'Projects'
        db.create_table('teamdb_projects', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('url_address', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_start', self.gf('django.db.models.fields.DateField')()),
            ('klient', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('teamdb', ['Projects'])

        # Adding model 'Price'
        db.create_table('teamdb_price', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('teamdb', ['Price'])

    def backwards(self, orm):
        # Deleting model 'Employee'
        db.delete_table('teamdb_employee')

        # Deleting model 'Projects'
        db.delete_table('teamdb_projects')

        # Deleting model 'Price'
        db.delete_table('teamdb_price')

    models = {
        'teamdb.employee': {
            'Meta': {'object_name': 'Employee'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'skils': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'specialization': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'teamdb.price': {
            'Meta': {'object_name': 'Price'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'teamdb.projects': {
            'Meta': {'object_name': 'Projects'},
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'klient': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'url_address': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['teamdb']