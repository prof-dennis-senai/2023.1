## Verificar autenticação:
```html
<ul class="navbar-nav ms-auto">
    {% if request.user.is_authenticated %}
    <li class="nav-item">
        <a class="nav-link" href="{% url 'logout' %}">Logout</a>
    </li>
    {% else %}
    <li class="nav-item">
        <a class="nav-link" href="{% url 'login' %}">Login</a>
    </li>
    {% endif %}
</ul>
```

## validar permissão
```html
{% if perms.app_produtos.add_produto %}
    <li class="nav-item">
        <a class="nav-link" href="{% url 'adicionar' %}">Cadastrar Produtos</a>
    </li>
{% endif %}
```

## criar permissão | grupo
```python
In [1]: from django.contrib.auth.models import Group, Permission
In [2]: from app_produtos.models import Produto
In [3]: grupo_vendedores, created = Group.objects.get_or_create(name='Vendedores')
In [4]: permissao_adicionar = Permission.objects.get(codename='add_produto')
In [5]: grupo_vendedores.permissions.add(permissao_adicionar)
In [6]: from django.contrib.auth.models import User
In [7]: usuario = User.objects.get(username='dennis')
In [8]: grupo_vendedores.user_set.add(usuario)
```


## criar permissão | usuário
```python
In [1]: from django.contrib.auth.models import Group, Permission
In [2]: from django.contrib.auth.models import User
In [3]: usuario = User.objects.get(username='usuario_exemplo')
In [4]: permissao_adicionar = Permission.objects.get(codename='add_produto')
In [5]: usuario.user_permissions.add(permissao_adicionar)
In [6]: usuario.save()
```