from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_groups(sender, **kwargs):
    try:
        print("Inside create_groups function...")

        # Create or get groups
        readers_group, readers_created = Group.objects.get_or_create(name="readers")
        author_group, author_created = Group.objects.get_or_create(name="author")
        
        print(f"Readers created? {readers_created}, Author created? {author_created}")

        # Get ContentType for Group model
        group_ct = ContentType.objects.get(app_label='auth', model='group')

        # Create custom permission (if not already exists)
        publish_perm, _ = Permission.objects.get_or_create(
            codename='publish_group',
            name='Can publish group',
            content_type=group_ct
        )

        # Safely get existing permissions
        view_perm = Permission.objects.get(codename='view_group')
        add_perm = Permission.objects.get(codename='add_group')
        change_perm = Permission.objects.get(codename='change_group')
        delete_perm = Permission.objects.get(codename='delete_group')

        # Assign permissions
        readers_group.permissions.set([view_perm])
        author_group.permissions.set([
            add_perm, change_perm, delete_perm, view_perm, publish_perm
        ])

        print("Groups and permissions successfully created.")

    except Exception as e:
        print(f"Error in create_groups: {e}")
