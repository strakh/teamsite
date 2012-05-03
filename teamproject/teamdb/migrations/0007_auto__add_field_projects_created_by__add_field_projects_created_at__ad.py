# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Projects.created_by'
        db.add_column('teamdb_projects', 'created_by',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Projects.created_at'
        db.add_column('teamdb_projects', 'created_at',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Projects.modified_by'
        db.add_column('teamdb_projects', 'modified_by',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Projects.modified_at'
        db.add_column('teamdb_projects', 'modified_at',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Image.created_by'
        db.add_column('teamdb_image', 'created_by',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Image.created_at'
        db.add_column('teamdb_image', 'created_at',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Image.modified_by'
        db.add_column('teamdb_image', 'modified_by',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Image.modified_at'
        db.add_column('teamdb_image', 'modified_at',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Employee.created_by'
        db.add_column('teamdb_employee', 'created_by',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Employee.created_at'
        db.add_column('teamdb_employee', 'created_at',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Employee.modified_by'
        db.add_column('teamdb_employee', 'modified_by',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Employee.modified_at'
        db.add_column('teamdb_employee', 'modified_at',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.created_by'
        db.add_column('teamdb_article', 'created_by',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.created_at'
        db.add_column('teamdb_article', 'created_at',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.modified_by'
        db.add_column('teamdb_article', 'modified_by',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.modified_at'
        db.add_column('teamdb_article', 'modified_at',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Projects.created_by'
        db.delete_column('teamdb_projects', 'created_by')

        # Deleting field 'Projects.created_at'
        db.delete_column('teamdb_projects', 'created_at')

        # Deleting field 'Projects.modified_by'
        db.delete_column('teamdb_projects', 'modified_by')

        # Deleting field 'Projects.modified_at'
        db.delete_column('teamdb_projects', 'modified_at')

        # Deleting field 'Image.created_by'
        db.delete_column('teamdb_image', 'created_by')

        # Deleting field 'Image.created_at'
        db.delete_column('teamdb_image', 'created_at')

        # Deleting field 'Image.modified_by'
        db.delete_column('teamdb_image', 'modified_by')

        # Deleting field 'Image.modified_at'
        db.delete_column('teamdb_image', 'modified_at')

        # Deleting field 'Employee.created_by'
        db.delete_column('teamdb_employee', 'created_by')

        # Deleting field 'Employee.created_at'
        db.delete_column('teamdb_employee', 'created_at')

        # Deleting field 'Employee.modified_by'
        db.delete_column('teamdb_employee', 'modified_by')

        # Deleting field 'Employee.modified_at'
        db.delete_column('teamdb_employee', 'modified_at')

        # Deleting field 'Article.created_by'
        db.delete_column('teamdb_article', 'created_by')

        # Deleting field 'Article.created_at'
        db.delete_column('teamdb_article', 'created_at')

        # Deleting field 'Article.modified_by'
        db.delete_column('teamdb_article', 'modified_by')

        # Deleting field 'Article.modified_at'
        db.delete_column('teamdb_article', 'modified_at')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'teamdb.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'article'", 'unique': 'True', 'null': 'True', 'to': "orm['teamdb.Employee']"}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'article'", 'unique': 'True', 'null': 'True', 'to': "orm['teamdb.Image']"}),
            'modified_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'teamdb.employee': {
            'Meta': {'object_name': 'Employee'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'employee'", 'unique': 'True', 'null': 'True', 'to': "orm['teamdb.Image']"}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'position_in_team': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'employee'", 'unique': 'True', 'null': 'True', 'to': "orm['auth.User']"})
        },
        'teamdb.image': {
            'Meta': {'object_name': 'Image'},
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'url': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'teamdb.projects': {
            'Meta': {'object_name': 'Projects'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': "orm['teamdb.Employee']"}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'modified_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'screenshots': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': "orm['teamdb.Image']"}),
            'url_address': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['teamdb']