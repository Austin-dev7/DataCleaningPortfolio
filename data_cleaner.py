import csv

def clean_csv(input_file, output_file):
    """
    Cleans a CSV file by removing empty rows, duplicates, and optionally filtering rows.
    """
    # Step 1: Read CSV and trim spaces
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        rows = []
        for row in reader:
            new_row = [cell.strip() for cell in row]  # Trim spaces
            if any(new_row):  # Skip empty rows
                rows.append(new_row)

    if not rows:
        print("CSV is empty!")
        return

    headers = rows[0]  # First row as headers
    data_rows = rows[1:]  # Data only

    print("\nColumns in your CSV:")
    for idx, col in enumerate(headers):
        print(f"{idx}: {col}")

    # Step 2: Choose column for duplicate removal
    col_input = input("\nEnter column name to remove duplicates by (or leave blank for entire row): ").strip()
    column_index = headers.index(col_input) if col_input in headers else None

    # Step 3: Optional row filter
    filter_input = input("Optional: filter rows (e.g., age>20) or leave blank: ").strip()
    filtered_rows = []
    if filter_input:
        try:
            col_name, condition = filter_input.split(">", 1)
            col_name = col_name.strip()
            column_index_filter = headers.index(col_name)
            threshold = float(condition.strip())
            for row in data_rows:
                try:
                    if float(row[column_index_filter]) > threshold:
                        filtered_rows.append(row)
                except:
                    pass  # skip if conversion fails
        except:
            print("Invalid filter. Ignoring filter.")
            filtered_rows = data_rows
    else:
        filtered_rows = data_rows

    # Step 4: Remove duplicates
    seen = set()
    unique_rows = []
    duplicate_rows = []

    for row in filtered_rows:
        key = row[column_index] if column_index is not None else tuple(row)
        if key not in seen:
            seen.add(key)
            unique_rows.append(row)
        else:
            duplicate_rows.append(row)

    # Step 5: Preview removed rows
    print("\nRows to be removed:")
    if duplicate_rows:
        print("Duplicate rows:")
        for r in duplicate_rows:
            print(r)
    else:
        print("No duplicate rows to remove!")

    # Step 6: Ask for confirmation
    confirm = input("\nDo you want to continue and save the cleaned CSV? (y/n): ").lower()
    if confirm != 'y':
        print("Cleaning cancelled. No file was saved.")
        return

    # Step 7: Write cleaned CSV
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        writer.writerows(unique_rows)

    # Step 8: Show stats
    print(f"\nRows before cleaning: {len(data_rows)}")
    print(f"Rows after cleaning: {len(unique_rows)}")
    print(f"Clean file saved as: {output_file}")

    # Step 9: Preview first 5 rows of cleaned CSV
    print("\nPreview of cleaned CSV (first 5 rows or less):")
    for row in unique_rows[:5]:
        print(row)


# --- Script starts here ---
if __name__ == "__main__":
    input_file = input("Enter input CSV filename (example: data.csv): ").strip()
    output_file = input("Enter output CSV filename (example: cleaned.csv): ").strip()
    clean_csv(input_file, output_file)