from django.conf import settings

BIRTH_YEAR_ERROR_MSG = "Tu'gilgan yil {min_year} dan katta va {max_year} dan kichik bo'lishi kerak.".format(min_year=settings.BIRTH_YEAR_MIN, max_year=settings.BIRTH_YEAR_MAX)
ACTIVE_USER_NOT_FOUND_ERROR_MSG = "Ushbu elektron pochta manzili bilan foydalanuvchi topilmadi!"




