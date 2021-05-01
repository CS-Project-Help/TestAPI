# users

## users/get_user/
По `id` получить информацию о пользователе(информация отображаемая на главной странице личного кабинета) 

#### Request:
> `id: UUID` - required

#### Response:
> `id: UUID` \
> `email: str` \
> `first_name: str` \
> `second_name: str` \
> `birthday: date` \
> `country: UUID` \
> ...(Все что будет храниться в `User`)

## users/create_user/
Создать пользователя(регистрация пользователя)

#### Request:
> `email: str` - required \
> `password: str` - required \
> `first_name: str` \
> `second_name: str` \
> `birthday: date` \
> `country: UUID` \
> ...(Все что будет храниться в `User`)

#### Response:
> `id: UUID` \
> `email: str`

## users/change_password/
Изменить пароль

#### Request:
> `id: UUID` - required \
> `old_password: str` - required \
> `new_password: str` - required

#### Response:
> `changed: bool`

## users/restore_password/

#### Request:
> `email: str` - required

#### Response:
> `restored: bool` \
> `message: str`

## users/create_new_password/
Восстановить пароль

#### Request:
> `id: str` - required \
> `new_password: str` - required

#### Response:
> `created: bool`

## users/login/
sign in

#### Request:
> `email: str` - required \
> `password: str` - required

#### Response:
> `{}`

## users/logout/
sign out

#### Request:
> `id: UUID`  - required

#### Response:
> `{}`

## users/update_profile/
Внести изменения в информацию о пользователе

#### Request:
> `id: UUID` - required \
> `first_name: str` \
> `second_name: str` \
> `birthday: date` \
> `country: UUID` \
> ...(Все что будет храниться в `User`)

#### Response:
> `{}`

## users/change_email/
сменить почту

#### Request:
> `id: UUID` - required \
> `new_email: str` - required

#### Response:
> `{}`

## users/donate_history/
История донатов пользователя

#### Request:
> `id: UUID` - required \
> `filters: dict` \
> `sorting: str`

#### Response:
> `items: list[Donate_history]`

## users/current_donations/
Текущие подписки пользователя

#### Request:
> `id: UUID` - required

#### Response:
> `items: list[Donate]`

# projects

## projects/get_projects/
Список проектов

#### Request:
> `filters: list` \
> `sorting: str`

#### Response:
> `items: list[Project]`

## projects/get_project/
Информация о проекте

#### Request:
> `id: UUID` - required

#### Response:
> `id: UUID` \
> `name: str` \
> `organization: fk_format` \
> `images: list` \
> `subject: str` \
> ...(Все что будет храниться в `Project`)

# organizations

## organiztions/get_organizations/
Список организаций

#### Request:
> `filters: list` \
> `sorting: str`

#### Request:
> `items: list[Organization]`

## organiztions/get_organization/
Информация об организации

#### Request:
> `id: UUID` - required

#### Response:
> `id: UUID` \
> `name: str` \
> `projects: list[fk_format]` \
> `images: list` \
> `subject: str` \
> ...(Все что будет храниться в `Organization`)

# donaties

## donaties/donate_organization/
Донат организации

#### Request:
> `id: UUID` - required \
> `organization: UUID` - required \
> `period: int`

#### Response:
> `{}`

## donaties/donate_project/
Донат организации

#### Request:
> `id: UUID` - required \
> `project: UUID` - required \
> `period: int`

#### Response:
> `{}`

## donaties/delete_donate/
Удалить периодический донат

#### Request:
> `id: UUID` - required

#### Response:
> `{}`

## donaties/update_donate/
Изменить донат

#### Request:
> `id: UUID` - required \
> `period: int` \
> `sum: NUMERIC`

#### Response:
> `{}`

# service

## country/get_countries/

#### Request:
> `{}`

#### Response::
> `items: list[Country]`