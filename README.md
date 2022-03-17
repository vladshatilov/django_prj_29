### Собственное «Авито». Django, GenericView, Postgres, Модели с relations и QuerySet
- Создал модели на основе фейковых данных, подключил к проекту PostgreSQL
- CBV и GenericViews
- CRUD для категорий, объявлений, пользователей и локаций. ForeignKey и ManyToManyField отношения
- Добавлена возможность загружать Media 

# Добавлено: 
## Сериализаторы и вьюсеты.
- Подключил к проекту DRF
- Добавил Location с использованием ViewSet и Router 
- Добавил Serializers
- Переписал Django GenericView на DRF (ListApiView и т.д.)
- Поиск по категориям, словам, географии, диапазону цен с использованием lookup's
