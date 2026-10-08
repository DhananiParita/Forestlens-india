import pandas as pd
import os

os.makedirs('data/processed', exist_ok=True)

def process_tree_loss(filepath, id_cols, output_filename):
    df = pd.read_excel(filepath)
    # Filter for standard forest canopy cover threshold (>= 30%)
    df_filtered = df[df['threshold'] == 30].copy()
    
    loss_cols = [c for c in df_filtered.columns if c.startswith('tc_loss_ha_')]
    
    df_long = pd.melt(
        df_filtered,
        id_vars=id_cols + ['area_ha', 'extent_2000_ha', 'extent_2010_ha', 'gain_2000-2012_ha'],
        value_vars=loss_cols,
        var_name='Year',
        value_name='Tree_Cover_Loss_ha'
    )
    df_long['Year'] = df_long['Year'].str.replace('tc_loss_ha_', '').astype(int)
    
    df_long.to_csv(f'data/processed/{output_filename}', index=False)
    print(f"Saved: data/processed/{output_filename}")

def process_carbon(filepath, id_cols, thresh_col, output_filename):
    df = pd.read_excel(filepath)
    df_filtered = df[df[thresh_col] == 30].copy()
    
    emission_cols = [c for c in df_filtered.columns if c.startswith('gfw_gross_emissions_co2e_all_gases_20')]
    
    df_long = pd.melt(
        df_filtered,
        id_vars=id_cols,
        value_vars=emission_cols,
        var_name='Year',
        value_name='CO2_Emissions_Mg'
    )
    df_long['Year'] = df_long['Year'].str.extract('(\d{4})').astype(int)
    
    df_long.to_csv(f'data/processed/{output_filename}', index=False)
    print(f"Saved: data/processed/{output_filename}")

# Run Transformations
process_tree_loss('data/raw/Country tree cover loss.xlsx', ['country'], 'country_loss.csv')
process_tree_loss('data/raw/Subnational 1 tree cover loss.xlsx', ['country', 'subnational1'], 'state_loss.csv')
process_tree_loss('data/raw/Subnational 2 tree cover loss.xlsx', ['country', 'subnational1', 'subnational2'], 'district_loss.csv')

process_carbon('data/raw/Country carbon data.xlsx', ['country'], 'umd_tree_cover_density__threshold', 'country_carbon.csv')
process_carbon('data/raw/Subnational 1 carbon data.xlsx', ['country', 'subnational1'], 'umd_tree_cover_density__threshold', 'state_carbon.csv')
process_carbon('data/raw/Subnational 2 carbon data.xlsx', ['country', 'subnational1', 'subnational2'], 'umd_tree_cover_density__threshold', 'district_carbon.csv')