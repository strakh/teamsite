# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Images'
        db.delete_table('teamdb_images')

        # Adding model 'Image'
        db.create_table('teamdb_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('url', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('teamdb', ['Image'])

        # Deleting field 'Projects.klient'
        db.delete_column('teamdb_projects', 'klient')

        # Adding field 'Projects.client'
        db.add_column('teamdb_projects', 'client',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field autors on 'Projects'
        db.delete_table('teamdb_projects_autors')

        # Adding M2M table for field authors on 'Projects'
        db.create_table('teamdb_projects_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projects', models.ForeignKey(orm['teamdb.projects'], null=False)),
            ('employee', models.ForeignKey(orm['teamdb.employee'], null=False))
        ))
        db.create_unique('teamdb_projects_authors', ['projects_id', 'employee_id'])

        # Adding M2M table for field screenshots on 'Projects'
        db.create_table('teamdb_projects_screenshots', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projects', models.ForeignKey(orm['teamdb.projects'], null=False)),
            ('image', models.ForeignKey(orm['teamdb.image'], null=False))
        ))
        db.create_unique('teamdb_projects_screenshots', ['projects_id', 'image_id'])


        # Changing field 'Projects.info'
        db.alter_column('teamdb_projects', 'info', self.gf('django.db.models.fields.TextField')())
        # Deleting field 'Employee.skils'
        db.delete_column('teamdb_employee', 'skils')

        # Deleting field 'Employee.user_no'
        db.delete_column('teamdb_employee', 'user_no_id')

        # Deleting field 'Employee.address'
        db.delete_column('teamdb_employee', 'address')

        # Deleting field 'Employee.date'
        db.delete_column('teamdb_employee', 'date')

        # Deleting field 'Employee.specialization'
        db.delete_column('teamdb_employee', 'specialization')

        # Adding field 'Employee.skype'
        db.add_column('teamdb_employee', 'skype',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Employee.jabber'
        db.add_column('teamdb_employee', 'jabber',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Employee.birth_date'
        db.add_column('teamdb_employee', 'birth_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Employee.position_in_team'
        db.add_column('teamdb_employee', 'position_in_team',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Employee.skills'
        db.add_column('teamdb_employee', 'skills',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Employee.user'
        db.add_column('teamdb_employee', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='employee', unique=True, null=True, to=orm['auth.User']),
                      keep_default=False)


        # Changing field 'Employee.info'
        db.alter_column('teamdb_employee', 'info', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Employee.img'
        db.alter_column('teamdb_employee', 'img_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['teamdb.Image']))
        # Deleting field 'Article.autor'
        db.delete_column('teamdb_article', 'autor_id')

        # Adding field 'Article.author'
        db.add_column('teamdb_article', 'author',
                      self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='article', unique=True, null=True, to=orm['teamdb.Employee']),
                      keep_default=False)

        # Adding field 'Article.img'
        db.add_column('teamdb_article', 'img',
                      self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='article', unique=True, null=True, to=orm['teamdb.Image']),
                      keep_default=False)

        # Removing M2M table for field img on 'Article'
        db.delete_table('teamdb_article_img')


        # Changing field 'Article.text'
        db.alter_column('teamdb_article', 'text', self.gf('django.db.models.fields.TextField')())
    def backwards(self, orm):
        # Adding model 'Images'
        db.create_table('teamdb_images', (
            ('url', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('teamdb', ['Images'])

        # Deleting model 'Image'
        db.delete_table('teamdb_image')


        # User chose to not deal with backwards NULL issues for 'Projects.klient'
        raise RuntimeError("Cannot reverse this migration. 'Projects.klient' and its values cannot be restored.")
        # Deleting field 'Projects.client'
        db.delete_column('teamdb_projects', 'client')

        # Adding M2M table for field autors on 'Projects'
        db.create_table('teamdb_projects_autors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projects', models.ForeignKey(orm['teamdb.projects'], null=False)),
            ('employee', models.ForeignKey(orm['teamdb.employee'], null=False))
        ))
        db.create_unique('teamdb_projects_autors', ['projects_id', 'employee_id'])

        # Removing M2M table for field authors on 'Projects'
        db.delete_table('teamdb_projects_authors')

        # Removing M2M table for field screenshots on 'Projects'
        db.delete_table('teamdb_projects_screenshots')


        # Changing field 'Projects.info'
        db.alter_column('teamdb_projects', 'info', self.gf('django.db.models.fields.CharField')(max_length=50))

        # User chose to not deal with backwards NULL issues for 'Employee.skils'
        raise RuntimeError("Cannot reverse this migration. 'Employee.skils' and its values cannot be restored.")
        # Adding field 'Employee.user_no'
        db.add_column('teamdb_employee', 'user_no',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Employee.address'
        raise RuntimeError("Cannot reverse this migration. 'Employee.address' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Employee.date'
        raise RuntimeError("Cannot reverse this migration. 'Employee.date' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Employee.specialization'
        raise RuntimeError("Cannot reverse this migration. 'Employee.specialization' and its values cannot be restored.")
        # Deleting field 'Employee.skype'
        db.delete_column('teamdb_employee', 'skype')

        # Deleting field 'Employee.jabber'
        db.delete_column('teamdb_employee', 'jabber')

        # Deleting field 'Employee.birth_date'
        db.delete_column('teamdb_employee', 'birth_date')

        # Deleting field 'Employee.position_in_team'
        db.delete_column('teamdb_employee', 'position_in_team')

        # Deleting field 'Employee.skills'
        db.delete_column('teamdb_employee', 'skills')

        # Deleting field 'Employee.user'
        db.delete_column('teamdb_employee', 'user_id')


        # Changing field 'Employee.info'
        db.alter_column('teamdb_employee', 'info', self.gf('django.db.models.fields.CharField')(max_length=600))

        # Changing field 'Employee.img'
        db.alter_column('teamdb_employee', 'img_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['teamdb.Images'], unique=True, null=True))
        # Adding field 'Article.autor'
        db.add_column('teamdb_article', 'autor',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['teamdb.Employee'], unique=True, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Article.author'
        db.delete_column('teamdb_article', 'author_id')

        # Deleting field 'Article.img'
        db.delete_column('teamdb_article', 'img_id')

        # Adding M2M table for field img on 'Article'
        db.create_table('teamdb_article_img', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm['teamdb.article'], null=False)),
            ('images', models.ForeignKey(orm['teamdb.images'], null=False))
        ))
        db.create_unique('teamdb_article_img', ['article_id', 'images_id'])


        # Changing field 'Article.text'
        db.alter_column('teamdb_article', 'text', self.gf('django.db.models.fields.CharField')(max_length=600))
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
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'article'", 'unique': 'True', 'null': 'True', 'to': "orm['teamdb.Image']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'teamdb.employee': {
            'Meta': {'object_name': 'Employee'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'employee'", 'unique': 'True', 'null': 'True', 'to': "orm['teamdb.Image']"}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'position_in_team': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'employee'", 'unique': 'True', 'null': 'True', 'to': "orm['auth.User']"})
        },
        'teamdb.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'url': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'teamdb.projects': {
            'Meta': {'object_name': 'Projects'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': "orm['teamdb.Employee']"}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'screenshots': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': "orm['teamdb.Image']"}),
            'url_address': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['teamdb']