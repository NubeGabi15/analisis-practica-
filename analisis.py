# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('C:\Users\Javig\OneDrive\Escritorio\practica1\Sample - Superstore.csv')

# Revisar datos
print("=== INFO ===")
print(df.info())

print("\n=== VALORES NULOS ===")
print(df.isnull().sum())

print("\n=== DUPLICADOS ===")
print(df.duplicated().sum())

# Limpiar
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])

print("\n✅ Limpieza completa!")
print("Filas finales: {len(df)}")

# ============================================
# ANALISIS EXPLORATORIO - EDA
# ============================================

# --- 1. Resumen general del dataset ---
print("\n=== PRIMERAS 5 FILAS ===")
print(df.head())

print("\n=== RESUMEN ESTADISTICO ===")
print(df[['Sales', 'Profit', 'Quantity', 'Discount']].describe())

# --- 2. Ventas por categoria ---
print("\n=== VENTAS POR CATEGORIA ===")
ventas_categoria = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(ventas_categoria)

# --- 3. Ganancia por categoria ---
print("\n=== GANANCIA POR CATEGORIA ===")
ganancia_categoria = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
print(ganancia_categoria)

# --- 4. Ventas por region ---
print("\n=== VENTAS POR REGION ===")
ventas_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(ventas_region)

# --- 5. Ventas por mes ---
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

print("\n=== VENTAS POR MES ===")
ventas_mes = df.groupby('Month')['Sales'].sum()
print(ventas_mes)

# --- 6. Top 5 productos mas vendidos ---
print("\n=== TOP 5 PRODUCTOS MAS VENDIDOS ===")
top_productos = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
print(top_productos)

# --- 7. Productos que pierden dinero ---
print("\n=== PRODUCTOS CON PERDIDA ===")
perdidas = df[df['Profit'] < 0].groupby('Category')['Profit'].sum().sort_values()
print(perdidas)


# ============================================
# GRAFICOS
# ============================================
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

# --- Grafico 1: Ventas por categoria ---
plt.figure(figsize=(8,5))
ventas_categoria.plot(kind='bar', color=['#2196F3','#FF9800','#4CAF50'])
plt.title('Ventas Totales por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Ventas ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('ventas_categoria.png')
plt.show()

# --- Grafico 2: Ventas por region ---
plt.figure(figsize=(8,5))
ventas_region.plot(kind='bar', color='#9C27B0')
plt.title('Ventas Totales por Region')
plt.xlabel('Region')
plt.ylabel('Ventas ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('ventas_region.png')
plt.show()

# --- Grafico 3: Ventas por mes ---
plt.figure(figsize=(10,5))
ventas_mes.plot(kind='line', marker='o', color='#F44336', linewidth=2)
plt.title('Tendencia de Ventas por Mes')
plt.xlabel('Mes')
plt.ylabel('Ventas ($)')
plt.xticks(range(1,13), ['Ene','Feb','Mar','Abr','May','Jun',
                          'Jul','Ago','Sep','Oct','Nov','Dic'])
plt.tight_layout()
plt.savefig('ventas_mes.png')
plt.show()

print("\nGraficos guardados!")