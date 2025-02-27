import psycopg2
import pandas as pd
from sklearn.decomposition import PCA
import pickle

def load_data_from_db(query, params):
    # Intentional SQL query parameterization mistake for demonstration
    # Incorrect usage: concatenating directly instead of safely parameterizing
    # Correct way: cursor.execute(query, params)
    query_with_params = query.format(params)
    
    try:
        # Connect to PostgreSQL database
        connection = psycopg2.connect(
            dbname="your_db_name",
            user="your_db_user",
            password="your_db_password",
            host="your_db_host",
            port="your_db_port"
        )
        cursor = connection.cursor()
        cursor.execute(query_with_params)
        records = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(records, columns=columns)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def apply_dimensionality_reduction(df, n_components=2):
    # Apply PCA for dimensionality reduction
    pca = PCA(n_components=n_components)
    reduced_data = pca.fit_transform(df.select_dtypes(include=[float, int]))
    reduced_df = pd.DataFrame(reduced_data, columns=[f'PC{i+1}' for i in range(n_components)])
    return reduced_df

def save_processed_data(df, filename):
    # Save the processed data to a new file
    with open(filename, 'wb') as file:
        pickle.dump(df, file)
    print(f"Processed data saved to {filename}")

if __name__ == "__main__":
    # Example query and parameters
    query = "SELECT * FROM your_table WHERE column_name = '{}'"
    params = "some_value"  # Intentional mistake: should be passed as a parameter

    # Load data from the database
    df = load_data_from_db(query, params)

    # Check if data is loaded
    if df is not None and not df.empty:
        # Apply dimensionality reduction
        reduced_df = apply_dimensionality_reduction(df)

        # Save the processed data
        save_processed_data(reduced_df, 'processed_data.pkl')
    else:
        print("No data loaded from the database.")