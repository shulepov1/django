# Generated by Django 4.2.5 on 2023-11-25 14:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Введите дату матча')),
                ('home_team_score', models.IntegerField(default=0, help_text='Введите счет хозяев', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
                ('away_team_score', models.IntegerField(default=0, help_text='Введите счет гостей', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите имя игрока', max_length=100)),
                ('position', models.CharField(choices=[('PG', 'Point Guard'), ('SG', 'Shooting Guard'), ('SF', 'Small Forward'), ('PF', 'Power Forward'), ('C', 'Center')], help_text='Позиция игрока', max_length=50)),
                ('jersey_number', models.IntegerField(default=1, help_text='Введите номер на его майке', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('id_user', models.ForeignKey(blank=True, help_text='выберите id пользователя', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название команды', max_length=100)),
                ('city', models.CharField(help_text='Из какого города команда', max_length=100)),
                ('conference', models.CharField(choices=[('WEST', 'Western'), ('EAST', 'Eastern')], help_text='Название конференции', max_length=50)),
                ('division', models.CharField(blank=True, help_text='Название дивизиона', max_length=50, null=True)),
                ('id_user', models.ForeignKey(blank=True, help_text='выберите id пользователя', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0, help_text='Введите количество очков', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
                ('rebounds', models.IntegerField(default=0, help_text='Введите количество подборов', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
                ('assists', models.IntegerField(default=0, help_text='Введите количество передач', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
                ('game', models.ForeignKey(help_text='Выберите игру', on_delete=django.db.models.deletion.CASCADE, to='myApp.game')),
                ('player', models.ForeignKey(help_text='Выберите игрока', on_delete=django.db.models.deletion.CASCADE, to='myApp.player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(help_text='Выберите команду', on_delete=django.db.models.deletion.CASCADE, to='myApp.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(help_text='Выберите "гостей" матча', on_delete=django.db.models.deletion.CASCADE, related_name='away_game', to='myApp.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(help_text='Выберите "хозяев" матча', on_delete=django.db.models.deletion.CASCADE, related_name='home_game', to='myApp.team'),
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('MVP', 'Most Valuable Player'), ('ROY', 'Rookie of the Year'), ('DPOY', 'Defensive Player of the Year'), ('6MOY', 'Sixth Man of the Year'), ('MIP', 'Most Improved Player')], help_text='Название награды', max_length=100)),
                ('year', models.IntegerField(choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)])),
                ('players', models.ManyToManyField(to='myApp.player')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together={('team', 'jersey_number')},
        ),
    ]
