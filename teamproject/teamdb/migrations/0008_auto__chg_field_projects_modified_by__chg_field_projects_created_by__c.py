# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Article', fields ['author']
        db.delete_unique('teamdb_article', ['author_id'])


        # Renaming column for 'Projects.modified_by' to match new field type.
        db.rename_column('teamdb_projects', 'modified_by', 'modified_by_id')
        # Changing field 'Projects.modified_by'
        db.alter_column('teamdb_projects', 'modified_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))
        # Adding index on 'Projects', fields ['modified_by']
        db.create_index('teamdb_projects', ['modified_by_id'])


        # Renaming column for 'Projects.created_by' to match new field type.
        db.rename_column('teamdb_projects', 'created_by', 'created_by_id')
        # Changing field 'Projects.created_by'
        db.alter_column('teamdb_projects', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))
        # Adding index on 'Projects', fields ['created_by']
        db.create_index('teamdb_projects', ['created_by_id'])


        # Renaming column for 'Image.modified_by' to match new field type.
        db.rename_column('teamdb_image', 'modified_by', 'modified_by_id')
        # Changing field 'Image.modified_by'
        db.alter_column('teamdb_image', 'modified_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))
        # Adding index on 'Image', fields ['modified_by']
        db.create_index('teamdb_image', ['modified_by_id'])


        # Renaming column for 'Image.created_by' to match new field type.
        db.rename_column('teamdb_image', 'created_by', 'created_by_id')
        # Changing field 'Image.created_by'
        db.alter_column('teamdb_image', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))
        # Adding index on 'Image', fields ['created_by']
        db.create_index('teamdb_image', ['created_by_id'])


        # Renaming column for 'Employee.modified_by' to match new field type.
        db.rename_column('teamdb_employee', 'modified_by', 'modified_by_id')
        # Changing field 'Employee.modified_by'
        db.alter_column('teamdb_employee', 'modified_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))
        # Adding index on 'Employee', fields ['modified_by']
        db.create_index('teamdb_employee', ['modified_by_id'])


        # Renaming column for 'Employee.created_by' to match new field type.
        db.rename_column('teamdb_employee', 'created_by', 'created_by_id')
        # Changing field 'Employee.created_by'
        db.alter_column('teamdb_employee', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))
        # Adding index on 'Employee', fields ['created_by']
        db.create_index('teamdb_employee', ['created_by_id'])

        # Deleting field 'Article.img'
        db.delete_column('teamdb_article', 'img_id')

        # Adding M2M table for field img on 'Article'
        db.create_table('teamdb_article_img', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm['teamdb.article'], null=False)),
            ('image', models.ForeignKey(orm['teamdb.image'], null=False))
        ))
        db.create_unique('teamdb_article_img', ['article_id', 'image_id'])


        # Renaming column for 'Article.modified_by' to match new field type.
        db.rename_column('teamdb_article', 'modified_by', 'modified_by_id')
        # Changing field 'Article.modified_by'
        db.alter_column('teamdb_article', 'modified_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))
        # Adding index on 'Article', fields ['modified_by']
        db.create_index('teamdb_article', ['modified_by_id'])


        # Changing field 'Article.author'
        db.alter_column('teamdb_article', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['teamdb.Employee']))

        # Renaming column for 'Article.created_by' to match new field type.
        db.rename_column('teamdb_article', 'created_by', 'created_by_id')
        # Changing field 'Article.created_by'
        db.alter_column('teamdb_article', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))
        # Adding index on 'Article', fields ['created_by']
        db.create_index('teamdb_article', ['created_by_id'])

    def backwards(self, orm):
        # Removing index on 'Article', fields ['created_by']
        db.delete_index('teamdb_article', ['created_by_id'])

        # Removing index on 'Article', fields ['modified_by']
        db.delete_index('teamdb_article', ['modified_by_id'])

        # Removing index on 'Employee', fields ['created_by']
        db.delete_index('teamdb_employee', ['created_by_id'])

        # Removing index on 'Employee', fields ['modified_by']
        db.delete_index('teamdb_employee', ['modified_by_id'])

        # Removing index on 'Image', fields ['created_by']
        db.delete_index('teamdb_image', ['created_by_id'])

        # Removing index on 'Image', fields ['modified_by']
        db.delete_index('teamdb_image', ['modified_by_id'])

        # Removing index on 'Projects', fields ['created_by']
        db.delete_index('teamdb_projects', ['created_by_id'])

        # Removing index on 'Projects', fields ['modified_by']
        db.delete_index('teamdb_projects', ['modified_by_id'])


        # Renaming column for 'Projects.modified_by' to match new field type.
        db.rename_column('teamdb_projects', 'modified_by_id', 'modified_by')
        # Changing field 'Projects.modified_by'
        db.alter_column('teamdb_projects', 'modified_by', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Renaming column for 'Projects.created_by' to match new field type.
        db.rename_column('teamdb_projects', 'created_by_id', 'created_by')
        # Changing field 'Projects.created_by'
        db.alter_column('teamdb_projects', 'created_by', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Renaming column for 'Image.modified_by' to match new field type.
        db.rename_column('teamdb_image', 'modified_by_id', 'modified_by')
        # Changing field 'Image.modified_by'
        db.alter_column('teamdb_image', 'modified_by', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Renaming column for 'Image.created_by' to match new field type.
        db.rename_column('teamdb_image', 'created_by_id', 'created_by')
        # Changing field 'Image.created_by'
        db.alter_column('teamdb_image', 'created_by', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Renaming column for 'Employee.modified_by' to match new field type.
        db.rename_column('teamdb_employee', 'modified_by_id', 'modified_by')
        # Changing field 'Employee.modified_by'
        db.alter_column('teamdb_employee', 'modified_by', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Renaming column for 'Employee.created_by' to match new field type.
        db.rename_column('teamdb_employee', 'created_by_id', 'created_by')
        # Changing field 'Employee.created_by'
        db.alter_column('teamdb_employee', 'created_by', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))
        # Adding field 'Article.img'
        db.add_column('teamdb_article', 'img',
                      self.gf('django.db.models.fields.related.OneToOneField')(related_name='article', unique=True, null=True, to=orm['teamdb.Image'], blank=True),
                      keep_default=False)

        # Removing M2M table for field img on 'Article'
        db.delete_table('teamdb_article_img')


        # Renaming column for 'Article.modified_by' to match new field type.
        db.rename_column('teamdb_article', 'modified_by_id', 'modified_by')
        # Changing field 'Article.modified_by'
        db.alter_column('teamdb_article', 'modified_by', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Article.author'
        db.alter_column('teamdb_article', 'author_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['teamdb.Employee']))
        # Adding unique constraint on 'Article', fields ['author']
        db.create_unique('teamdb_article', ['author_id'])


        # Renaming column for 'Article.created_by' to match new field type.
        db.rename_column('teamdb_article', 'created_by_id', 'created_by')
        # Changing field 'Article.created_by'
        db.alter_column('teamdb_article', 'created_by', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))
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
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'article'", 'null': 'True', 'to': "orm['teamdb.Employee']"}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'article_relate'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['teamdb.Image']"}),
            'modified_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'article_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'teamdb.employee': {
            'Meta': {'object_name': 'Employee'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'employee_relate'", 'null': 'True', 'to': "orm['auth.User']"}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'employee'", 'unique': 'True', 'null': 'True', 'to': "orm['teamdb.Image']"}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'employee_related'", 'null': 'True', 'to': "orm['auth.User']"}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'image_relate'", 'null': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'image_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'url': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'teamdb.projects': {
            'Meta': {'object_name': 'Projects'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': "orm['teamdb.Employee']"}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'projects_relate'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'modified_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'projects_related'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'screenshots': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': "orm['teamdb.Image']"}),
            'url_address': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['teamdb']