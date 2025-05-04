# AI Agent Insight Report
**Dataset:** E-Commerce Sales Dataset

**Description:** Analyzing and Maximizing Online Business Performance

**Generated on:** 2025-05-02 09:42

## Dataset Overview
- Shape: (128975, 24)
- Columns: ['index', 'Order ID', 'Date', 'Status', 'Fulfilment', 'Sales Channel ', 'ship-service-level', 'Style', 'SKU', 'Category', 'Size', 'ASIN', 'Courier Status', 'Qty', 'currency', 'Amount', 'ship-city', 'ship-state', 'ship-postal-code', 'ship-country', 'promotion-ids', 'B2B', 'fulfilled-by', 'Unnamed: 22']
- Data Types: {'index': 'int64', 'Order ID': 'object', 'Date': 'object', 'Status': 'object', 'Fulfilment': 'object', 'Sales Channel ': 'object', 'ship-service-level': 'object', 'Style': 'object', 'SKU': 'object', 'Category': 'object', 'Size': 'object', 'ASIN': 'object', 'Courier Status': 'object', 'Qty': 'int64', 'currency': 'object', 'Amount': 'float64', 'ship-city': 'object', 'ship-state': 'object', 'ship-postal-code': 'float64', 'ship-country': 'object', 'promotion-ids': 'object', 'B2B': 'bool', 'fulfilled-by': 'object', 'Unnamed: 22': 'bool'}

## Basic Statistics
**index**: {'count': 128975.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 64487.0, 'std': 37232.019821653514, 'min': 0.0, '25%': 32243.5, '50%': 64487.0, '75%': 96730.5, 'max': 128974.0}

**Order ID**: {'count': 128975, 'unique': 120378, 'top': '171-5057375-2831560', 'freq': 12, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**Date**: {'count': 128975, 'unique': 91, 'top': '05-03-22', 'freq': 2085, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**Status**: {'count': 128975, 'unique': 13, 'top': 'Shipped', 'freq': 77804, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**Fulfilment**: {'count': 128975, 'unique': 2, 'top': 'Amazon', 'freq': 89698, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**Sales Channel **: {'count': 128975, 'unique': 2, 'top': 'Amazon.in', 'freq': 128851, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**ship-service-level**: {'count': 128975, 'unique': 2, 'top': 'Expedited', 'freq': 88615, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**Style**: {'count': 128975, 'unique': 1377, 'top': 'JNE3797', 'freq': 4224, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**SKU**: {'count': 128975, 'unique': 7195, 'top': 'JNE3797-KR-L', 'freq': 773, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**Category**: {'count': 128975, 'unique': 9, 'top': 'Set', 'freq': 50284, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**Size**: {'count': 128975, 'unique': 11, 'top': 'M', 'freq': 22711, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**ASIN**: {'count': 128975, 'unique': 7190, 'top': 'B09SDXFFQ1', 'freq': 773, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**Courier Status**: {'count': 128975, 'unique': 3, 'top': 'Shipped', 'freq': 116359, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**Qty**: {'count': 128975.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.9044310912967629, 'std': 0.3133535856501447, 'min': 0.0, '25%': 1.0, '50%': 1.0, '75%': 1.0, 'max': 15.0}

**currency**: {'count': 128975, 'unique': 1, 'top': 'INR', 'freq': 128975, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**Amount**: {'count': 128975.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 645.9286939329328, 'std': 272.77882866610685, 'min': 0.0, '25%': 459.0, '50%': 605.0, '75%': 771.0, 'max': 5584.0}

**ship-city**: {'count': 128975, 'unique': 8955, 'top': 'BENGALURU', 'freq': 11250, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**ship-state**: {'count': 128975, 'unique': 69, 'top': 'MAHARASHTRA', 'freq': 22293, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**ship-postal-code**: {'count': 128975.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 463975.4646792014, 'std': 191453.1362303151, 'min': 110001.0, '25%': 382421.0, '50%': 500033.0, '75%': 600024.0, 'max': 989898.0}

**ship-country**: {'count': 128975, 'unique': 1, 'top': 'IN', 'freq': 128975, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**promotion-ids**: {'count': 128975, 'unique': 5787, 'top': 'IN Core Free Shipping 2015/04/08 23-48-5-108', 'freq': 95253, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**B2B**: {'count': 128975, 'unique': 2, 'top': False, 'freq': 128104, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**fulfilled-by**: {'count': 128975, 'unique': 1, 'top': 'Easy Ship', 'freq': 128975, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

**Unnamed: 22**: {'count': 128975, 'unique': 1, 'top': False, 'freq': 128975, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}

## Missing Values

## Key Insights
1. Column 'Qty' has 388 outliers (z-score > 3).
2. Mean of 'index' decreases with 'Fulfilment'.
3. Most common value in 'index' is '0'.
4. Column 'index' has all unique values (possible ID field).
