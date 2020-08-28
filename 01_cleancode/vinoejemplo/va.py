import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

media_alcohol = df.alcohol.median()
for i, alcohol in enumerate(df.alcohol):
    if alcohol >= media_alcohol:
        df.loc[i, 'alcohol'] = 'alto'
    else:
        df.loc[i, 'alcohol'] = 'bajo'
df.groupby('alcohol').quality.mean()

media_pH = df.pH.median()
for i, pH in enumerate(df.pH):
    if pH >= media_pH:
        df.loc[i, 'pH'] = 'alto'
    else:
        df.loc[i, 'pH'] = 'bajo'
df.groupby('pH').quality.mean()

media_azucar_residual = df.residual_sugar.median()
for i, sugar in enumerate(df.residual_sugar):
    if sugar >= media_azucar_residual:
        df.loc[i, 'residual sugar'] = 'alto'
    else:
        df.loc[i, 'residual sugar'] = 'bajo'
df.groupby('residual sugar').quality.mean()

mcamedia_acido_citrico = df.citric acid.median()
for i, citric acid in enumerate(df.citric acid):
    if citric acid >= media_acido_citrico:
        df.loc[i, 'citric acid'] = 'alto'
    else:
        df.loc[i, 'citric acid'] = 'bajo'
df.groupby('citric acid').quality.mean()