import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec



# Load Data

var1 = pd.read_csv("/Users/riteshsinghbisht/Downloads/drive-download-20251022T154651Z-1-001/blinkit_data.csv")



# Display first 5 rows of data

print(var1.head())



# All columns name

x = var1.columns

print(x ," \n")



# Data Cleaning

var1["Item Fat Content"] = var1["Item Fat Content"].replace({'low fat': "Low Fat", 
                                                             'LF' : "Low Fat",
                                                             "reg":"Regular"})



# ================================ Business Requirements ===========================================


# Total Sales: The overall revenue generated from all items sold.

total_sales = var1["Sales"].sum()

print(f"The total sales from all the items: ${total_sales:,.0f}" )



# Average Sales: The average revenue per sale.

avg_sales = round(var1["Sales"].mean(),2)

print(f"The avg sales from all the items: ${avg_sales:,.0f}")



# Number of Items: The total count of different items sold.

no_items = var1["Item Type"].count()

print(f"Total No of Items Sold: {no_items:,}")



# Average Rating: The average customer rating for items sold.

avg_rating = round(var1["Rating"].mean(),2)

print(f"The avgerage customer rating on items: {avg_rating}")



# ================================ Charts Requirements ===========================================

# Blinkit brand colors
blinkit_colors = ['#F8CB46', '#000000', '#FFFFFF']  # Yellow, Black, White

# Or use similar colors for your plots
blinkit_palette = ['#FFD700', '#00A859', '#FFA500','#FF6B35', '#FFA500']  # Yellow/Orange gradient


plot_path = '/Users/riteshsinghbisht/Desktop/Python/project/blinkit analysis/Plots/'

# 1. Total Sales by Fat Content:
#	Objective: Analyze the impact of fat content on total sales.
#	Additional KPI Metrics: Assess how other KPIs (Average Sales, Number of Items, Average Rating) 
#   vary with fat content.
#	Chart Type: Donut Chart.


sales_by_fat_content = var1.groupby("Item Fat Content")["Sales"].sum()
avg_sales_by_fat_content = var1.groupby("Item Fat Content")["Sales"].mean()
no_of_items_by_fat_content = var1.groupby("Item Fat Content")["Sales"].count()
avg_rating_by_fat_content = var1.groupby("Item Fat Content")["Rating"].mean()


# First Plot
n1 = plt.pie(sales_by_fat_content, 
       labels=sales_by_fat_content.index, 
       autopct='%1.1f%%', 
       startangle=90,
       wedgeprops={'edgecolor': 'black', 'linewidth': 1}, colors= blinkit_palette)

plt.title("Total Fat content distribution", fontsize=16, fontweight="bold",pad=10)
plt.xlabel("Fat content", fontsize=10, fontweight="bold",labelpad=10)

plt.tight_layout()
plt.savefig(f"{plot_path}Total Fat content distribution.png",dpi=300,bbox_inches='tight')
plt.show()


# Second Plot
bars = plt.bar(avg_sales_by_fat_content.index, 
               height=avg_sales_by_fat_content.values, 
               color=blinkit_palette, edgecolor='black')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f'{height:.1f}',
             ha='center', va='bottom')

plt.ylim(top= 200)
plt.title("Avg Fat content distribution",fontsize=16,fontweight='bold',pad=10)
plt.xlabel("Fat content", fontsize=10, fontweight="bold",labelpad=10)
plt.ylabel("Avg sales", fontsize=10, fontweight="bold",labelpad=10)
plt.tick_params(axis='both', which='major', labelsize=8)
for label in plt.gca().get_xticklabels() + plt.gca().get_yticklabels():
    label.set_fontweight('bold')

plt.tight_layout()
plt.savefig(f"{plot_path}Avg Fat content distribution.png",dpi=300,bbox_inches='tight')
plt.show()


# Third Plot
bars2 = plt.bar(no_of_items_by_fat_content.index, 
               height= no_of_items_by_fat_content.values, 
               color=blinkit_palette, edgecolor='black')

for bar in bars2:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f'{height:.0f}',
             ha='center', va='bottom')

plt.ylim(top= 6500)
plt.title("No of purchases by Fat content",fontsize=16,fontweight='bold',pad=10)
plt.xlabel("Fat content", fontsize=10, fontweight="bold",labelpad=10)
plt.ylabel("No of Purchase", fontsize=10, fontweight="bold",labelpad=10)
plt.tick_params(axis='both', which='major', labelsize=8)
for label in plt.gca().get_xticklabels() + plt.gca().get_yticklabels():
    label.set_fontweight('bold')

plt.tight_layout()
plt.savefig(f"{plot_path}No of purchases by Fat content.png",dpi=300,bbox_inches='tight')
plt.show()


# Forth Plot
bars3 = plt.bar(avg_rating_by_fat_content.index, 
               height= avg_rating_by_fat_content.values, 
               color=blinkit_palette, edgecolor='black')

for bar in bars3:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f'{height:.4f}',
             ha='center', va='bottom')

plt.ylim(top= 5)
plt.title("Avg Rating by Fat content",fontsize=16,fontweight='bold',pad=10)
plt.xlabel("Fat content", fontsize=10, fontweight="bold",labelpad=10)
plt.ylabel("Avg Rating", fontsize=10, fontweight="bold",labelpad=10)
plt.tick_params(axis='both', which='major', labelsize=8)
for label in plt.gca().get_xticklabels() + plt.gca().get_yticklabels():
    label.set_fontweight('bold')

plt.tight_layout()
plt.savefig(f"{plot_path}Avg Rating by Fat content.png",dpi=300,bbox_inches='tight')
plt.show()



# combined analysis - Fat content

fig, ax = plt.subplots(2,2, figsize=[10,6])

# First Plot
ax1  = ax[0,0]
ax1.pie(sales_by_fat_content, 
       labels=sales_by_fat_content.index, 
       autopct='%1.1f%%', 
       startangle=180,
       wedgeprops={'edgecolor': 'black', 'linewidth': 1}, colors= blinkit_palette)

ax1.set_title("Total Fat content distribution", fontsize=10, fontweight="bold",pad=10)

for spine in ax1.spines.values():
    spine.set_edgecolor('black')
    spine.set_linewidth(20)
    spine.set_visible(True)


# Second Plot
ax2 = ax[0,1]
bars = ax2.bar(avg_sales_by_fat_content.index, 
               height=avg_sales_by_fat_content.values, 
               color=blinkit_palette, edgecolor='black')

for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, height,
             f'{height:.1f}',
             ha='center', va='bottom')

ax2.set_ylim(top= 200)
ax2.set_title("Avg Fat content distribution",fontsize=10,fontweight='bold',pad=10)
ax2.set_ylabel("Avg sales", fontsize=8, fontweight="bold",labelpad=10)
ax2.tick_params(axis='both', which='major', labelsize=8)
for label in ax2.get_xticklabels() + ax2.get_yticklabels():
    label.set_fontweight('bold')


# Third Plot
ax3 = ax[1,0]
bars2 = ax3.bar(no_of_items_by_fat_content.index, 
               height= no_of_items_by_fat_content.values, 
               color=blinkit_palette, edgecolor='black')

for bar in bars2:
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2, height,
             f'{height:.0f}',
             ha='center', va='bottom')

ax3.set_ylim(top= 6500)
ax3.set_title("No of purchases by Fat content",fontsize=10,fontweight='bold',pad=10)
ax3.set_ylabel("No of Purchase", fontsize=8, fontweight="bold",labelpad=10)
ax3.tick_params(axis='both', which='major', labelsize=8)
for label in ax3.get_xticklabels() + ax3.get_yticklabels():
    label.set_fontweight('bold')


# Forth Plot
ax4 = ax[1,1]
bars3 = ax4.bar(avg_rating_by_fat_content.index, 
               height= avg_rating_by_fat_content.values, 
               color=blinkit_palette, edgecolor='black')

for bar in bars3:
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2, height,
             f'{height:.4f}',
             ha='center', va='bottom')

ax4.set_ylim(top= 5)
ax4.set_title("Avg Rating by Fat content",fontsize=10,fontweight='bold',pad=10)
ax4.set_ylabel("Avg Rating", fontsize=8, fontweight="bold",labelpad=10)
ax4.tick_params(axis='both', which='major', labelsize=8)
for label in ax4.get_xticklabels() + ax4.get_yticklabels():
    label.set_fontweight('bold')

fig.suptitle("Fat Content Analysis",fontsize= 16, fontweight='bold')

plt.tight_layout(h_pad= 3, w_pad= 3)
plt.savefig(f"{plot_path}Combined analysis - Fat content.png",dpi=300,bbox_inches='tight')
plt.show()



# 2. Total Sales by Item Type:
# 	Objective: Identify the performance of different item types in terms of total sales.
# 	Additional KPI Metrics: Assess how other KPIs (Average Sales, Number of Items, Average Rating) 
#     vary with fat content.
# 	Chart Type: Bar Chart.

blinkit_palette_extended = [
    '#FFE44D',  # 1. Light Yellow
    '#FFD700',  # 2. Gold
    '#F8CB46',  # 3. Blinkit Yellow 
    '#B8B8B8',  # 4. Light Grey (better visibility)
    '#808080',  # 5. Medium Grey
    '#4A4A4A',  # 6. Dark Grey
    '#1A1A1A',  # 7. Deep Black
    '#00D873',  # 8. Bright Green
    '#00C26F',  # 9. Light Green
    '#00B050',  # 10. Medium Green
    '#00A859',  # 11. Blinkit Green 
    '#00A04B',  # 12. Kelly Green
    '#008F4C',  # 13. Forest Green
    '#1A5D3A',  # 14. Dark Forest Green
    '#FF9500',  # 15. Amber
    '#FFA500'   # 16. Orange
]

Total_Sales_by_Item_Type = round(var1.groupby('Item Type')['Sales'].sum().sort_values(ascending=False),2)
Avg_Sales_by_Item_Type = round(var1.groupby('Item Type')['Sales'].mean().sort_values(ascending=False),2)
Total_no_of_Item_Type = round(var1.groupby('Item Type')['Sales'].count().sort_values(ascending=False),2)
Avg_rating_of_Item_Type = round(var1.groupby('Item Type')['Rating'].mean().sort_values(ascending=False),2)


# First Plot
plt.figure(figsize=(12,6))
sns.barplot(y=Total_Sales_by_Item_Type.index,
            x=Total_Sales_by_Item_Type.values,
            hue=Total_Sales_by_Item_Type.index,
            legend=False, palette= blinkit_palette_extended, 
            edgecolor='black')

plt.title("Total Sales by Item Type",fontsize= 16, fontweight = 'bold',pad=10)
plt.ylabel("Item Type",fontsize=10, fontweight='bold',labelpad =10)
plt.xlabel("Sales",fontsize=10, fontweight='bold',labelpad =10)
plt.tight_layout()
plt.savefig(f"{plot_path}Total Sales by Item Type.png",dpi=300,bbox_inches='tight')
plt.show()


# Second Plot
sns.barplot(x=Avg_Sales_by_Item_Type.index,
            y=Avg_Sales_by_Item_Type.values,
            hue=Avg_Sales_by_Item_Type.index,
            legend=False, palette= blinkit_palette_extended, edgecolor='black')

plt.title("Avg Sales by Item Type",fontsize= 16, fontweight = 'bold',pad=10)
plt.xlabel("Item Type",fontsize=10, fontweight='bold',labelpad =10)
plt.ylabel("AVG Sales",fontsize=10, fontweight='bold',labelpad =10)
plt.xticks(rotation=90)
plt.ylim(top=200)
plt.tight_layout()
plt.savefig(f"{plot_path}Avg Sales by Item Type.png",dpi=300,bbox_inches='tight')
plt.show()


# Third Plot
sns.barplot(y=Total_no_of_Item_Type.index, x= Total_no_of_Item_Type.values,
            hue=Total_no_of_Item_Type.index, palette= blinkit_palette_extended,
            edgecolor='black')
plt.xlim(right=1400)
plt.xlabel("No of purchase",fontsize=10,fontweight='bold',labelpad=10)
plt.ylabel("Item Type",fontsize=10,fontweight='bold')
plt.tight_layout()
plt.title("No of purchases per Item",fontsize=16,fontweight='bold',pad=10)
plt.tight_layout()
plt.savefig(f"{plot_path}No of purchases per Item.png",dpi=300,bbox_inches='tight')
plt.show()


# Forth Plot
abv_rating = sns.barplot(x=Avg_rating_of_Item_Type.index,
            y=Avg_rating_of_Item_Type.values,
            hue=Avg_rating_of_Item_Type.index,
            legend=False, palette= blinkit_palette_extended,edgecolor='black')

for bar in abv_rating.patches:
    abv_rating.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{bar.get_height():.2f}',
        ha='center',
        va='bottom',
        fontsize=9,
        fontweight='bold'
    )

plt.yticks([])
plt.title("Avg Sales by Item Type",fontsize= 16, fontweight = 'bold',pad=10)
plt.xlabel("Item Type",fontsize=10, fontweight='bold',labelpad =10)
plt.ylabel("AVG Rating",fontsize=10, fontweight='bold',labelpad =10)
plt.xticks(rotation=90)
plt.ylim(top=5)
plt.tight_layout()
plt.savefig(f"{plot_path}Avg Sales by Item Type.png",dpi=300,bbox_inches='tight')
plt.show()


# combined analysis - Item Type

fig, ax = plt.subplots(2,2,figsize=(12,10))

ax1 = ax[0,0]
ax2 = ax[0,1]
ax3 = ax[1,0]
ax4 = ax[1,1]

# First Plot
f1 = sns.barplot(y=Total_Sales_by_Item_Type.index,
            x=Total_Sales_by_Item_Type.values,
            hue=Total_Sales_by_Item_Type.index,
            legend=False, palette=blinkit_palette_extended,
            edgecolor='black', ax=ax1)

f1.set_title("Total_Sales_by_Item_Type",fontsize= 16, fontweight = 'bold',pad=10)
f1.set_ylabel("Item Type",fontsize=10, fontweight='bold',labelpad =10)
f1.set_xlabel("Sales",fontsize=10, fontweight='bold',labelpad =10)


# Second Plot
f2 = sns.barplot(x=Avg_Sales_by_Item_Type.index,
            y=Avg_Sales_by_Item_Type.values,
            hue=Avg_Sales_by_Item_Type.index,
            legend=False, palette=blinkit_palette_extended,
            edgecolor='black', ax=ax2)

for bar in f2.patches:
    f2.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{bar.get_height():.0f}',
        ha='center',
        va='bottom',
        fontsize=7,
        fontweight='bold'
    )
f2.set_yticks([])
f2.set_title("Avg Sales by Item Type",fontsize= 16, fontweight = 'bold',pad=10)
f2.set_ylabel("AVG Sales",fontsize=10, fontweight='bold',labelpad =10)
f2.tick_params(axis='x', rotation=90)
f2.set_ylim(top=200)


# Third Plot
f3 = sns.barplot(y=Total_no_of_Item_Type.index, x= Total_no_of_Item_Type.values,
            hue=Total_no_of_Item_Type.index, palette=blinkit_palette_extended,
            edgecolor='black', ax=ax3)
f3.set_xlim(right=1400)
f3.set_xlabel("No of purchase",fontsize=10,fontweight='bold',labelpad=10)
f3.set_ylabel("Item Type",fontsize=10,fontweight='bold')
f3.set_title("No of purchases per Item",fontsize=16,fontweight='bold',pad=10)


# Fourth Plot
f4 = sns.barplot(x=Avg_rating_of_Item_Type.index,
            y=Avg_rating_of_Item_Type.values,
            hue=Avg_rating_of_Item_Type.index,
            legend=False, palette=blinkit_palette_extended,edgecolor='black',ax=ax4)

for bar in f4.patches:
    f4.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{bar.get_height():.2f}',
        ha='center',
        va='bottom',
        fontsize=7,
        fontweight='bold'
    )

f4.set_yticks([])
f4.set_title("Avg Sales by Item Type",fontsize= 16, fontweight = 'bold',pad=10)
f4.set_xlabel("Item Type",fontsize=10, fontweight='bold',labelpad =10)
f4.set_ylabel("AVG Rating",fontsize=10, fontweight='bold',labelpad =10)
f4.tick_params(axis='x', rotation=90)
f4.set_ylim(top=5)
fig.suptitle("Item Type Analysis",fontsize=22, fontweight='bold', y=.99)

plt.tight_layout()
plt.savefig(f"{plot_path}Combined analysis - Item Type.png",dpi=300,bbox_inches='tight')
plt.show()



# 3. Fat Content by Outlet for Total Sales:
# 	Objective: Compare total sales across different outlets segmented by fat content.
# 	Additional KPI Metrics: Assess how other KPIs (Average Sales, Number of Items, 
#     Average Rating) vary with fat content.
# 	Chart Type: Stacked Column Chart.


# Group data
Total_sales_by_Outlet_Location = var1.groupby(["Outlet Location Type", "Item Fat Content"])["Sales"].sum().unstack()
Avg_sales_by_Outlet_Location =var1.groupby(['Outlet Location Type','Item Fat Content'])["Sales"].mean().unstack()
No_of_items_by_Outlet_Location = var1.groupby(['Outlet Location Type','Item Fat Content'])["Sales"].count().unstack()
Avg_rating_by_Outlet_Location = var1.groupby(['Outlet Location Type','Item Fat Content'])["Rating"].mean().unstack()

# First Plot 
Total_sales_by_Outlet_Location.plot(kind='bar', figsize=(10, 6), 
                                    color=blinkit_palette, edgecolor='black')
plt.title("Sales by Outlet Location Type and Fat Content", fontsize=16, fontweight='bold')
plt.xlabel("Outlet Location Type", fontweight='bold')
plt.ylabel("Sales", fontweight='bold')
plt.legend(title='Fat Content')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{plot_path}Sales by Outlet Location Type and Fat Content.png",dpi=300,bbox_inches='tight')
plt.show()

# Second Plot
Avg_sales_by_Outlet_Location.plot(kind="bar", figsize=(10, 6), 
                                  color=blinkit_palette, edgecolor='black')
plt.title("Avg Sales by Outlet Location Type and Fat Content", fontsize=16, fontweight='bold')
plt.xlabel("Outlet Location Type", fontweight='bold')
plt.ylabel("Avg Sales", fontweight='bold')
plt.legend(title='Fat Content')
plt.xticks(rotation=0)
plt.ylim(top=180)
plt.tight_layout()
plt.savefig(f"{plot_path}Avg Sales by Outlet Location Type and Fat Content.png",dpi=300,bbox_inches='tight')
plt.show()

# Third Plot
No_of_items_by_Outlet_Location.plot(kind="bar",figsize=(10,6),
                                    color=blinkit_palette, edgecolor='black')
plt.title("No of Purchase by Outlet Location Type and Fat Content",fontsize=16, fontweight='bold')
plt.xticks(rotation=0)
plt.legend(title="Fat Content")
plt.xlabel("Outlet Location Type", fontweight='bold')
plt.ylabel("No of Purchase", fontweight='bold')
plt.tight_layout()
plt.savefig(f"{plot_path}No of Purchase by Outlet Location Type and Fat Content.png",dpi=300,bbox_inches='tight')
plt.show()

# Fourth Plot
ab1 = Avg_rating_by_Outlet_Location.plot(kind="bar",figsize=(10,6),
                                         color=blinkit_palette, edgecolor='black')
plt.title("Avg Rating by Outlet Location Type and Fat Content",fontsize=16, fontweight='bold')
plt.xticks(rotation=0)
plt.legend(title="Fat Content")
plt.xlabel("Outlet Location Type", fontweight='bold')
plt.ylabel("Avg Rating", fontweight='bold')
plt.ylim(top=5.5)
plt.yticks([])

for bar in ab1.patches:
    ab1.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{bar.get_height():.2f}',
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

plt.tight_layout()
plt.savefig(f"{plot_path}Avg Rating by Outlet Location Type and Fat Content.png",dpi=300,bbox_inches='tight')
plt.show()


# combined analysis - Outlet Location Type

fig, ax = plt.subplots(2,2,figsize=(12,10))

ab1 = ax[0,0]
ab2 = ax[0,1]
ab3 = ax[1,0]
ab4 = ax[1,1]

# First Plot 
Ts = Total_sales_by_Outlet_Location.plot(kind='bar', 
                                    color=blinkit_palette, 
                                    edgecolor='black', ax=ab1)
Ts.set_title("Sales by Outlet Location Type and Fat Content", fontsize=10, fontweight='bold')
Ts.set_ylabel("Sales", fontweight='bold')
Ts.legend(title='Fat Content')
Ts.set_xlabel("")
Ts.tick_params(axis='x', rotation=0)

# Second Plot
As = Avg_sales_by_Outlet_Location.plot(kind="bar", 
                                  color=blinkit_palette, 
                                  edgecolor='black', ax=ab2, legend=False)
As.set_title("Avg Sales by Outlet Location Type and Fat Content", fontsize=10, fontweight='bold')
As.set_ylabel("Avg Sales", fontweight='bold')
As.tick_params(axis='x', rotation=0)
As.set_xlabel("")
As.set_ylim(top=180)

# Third Plot
CO = No_of_items_by_Outlet_Location.plot(kind="bar",
                                    color=blinkit_palette, 
                                    edgecolor='black', ax=ab3, legend=False)
CO.set_title("No of Purchase by Outlet Location Type and Fat Content",fontsize=10, fontweight='bold')
CO.tick_params(axis='x', rotation=0)
CO.set_xlabel("Outlet Location Type", fontweight='bold')
CO.set_ylabel("No of Purchase", fontweight='bold')

# Fourth Plot
AR = Avg_rating_by_Outlet_Location.plot(kind="bar",
                                         color=blinkit_palette, 
                                         edgecolor='black', ax=ab4, legend=False)
AR.set_title("Avg Rating by Outlet Location Type and Fat Content",fontsize=10, fontweight='bold')
AR.tick_params(axis='x', rotation=0)
AR.set_xlabel("Outlet Location Type", fontweight='bold')
AR.set_ylabel("Avg Rating", fontweight='bold')
AR.set_ylim(top=5.5)
AR.set_yticks([])

for bar in AR.patches:
    AR.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{bar.get_height():.2f}',
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

plt.tight_layout(h_pad=5, w_pad= 5)
plt.savefig(f"{plot_path}Combined analysis - Outlet Location Type.png",dpi=300,bbox_inches='tight')
plt.show()



# 4. Total Sales by Outlet Establishment:
# 	Objective: Evaluate how the age or type of outlet establishment influences total sales.
# 	Chart Type: Line Chart.

Total_sales_by_outlet_establishment = var1.groupby("Outlet Establishment Year")["Sales"].sum()

plt.figure(figsize=(8,6))
ax1 = sns.lineplot(x= Total_sales_by_outlet_establishment.index,
             y= Total_sales_by_outlet_establishment.values,
             marker="o", markersize=10, linestyle='--',
             color = '#F8CB46',
             markeredgecolor='black')
plt.ylim(top=240000)
plt.xlabel("Outlet Establishment Year", fontsize=10, fontweight='bold',labelpad=10)
plt.ylabel("Sales", fontsize=10, fontweight='bold',labelpad=10)
plt.title("Total Sales by Outlet Establishment", fontsize=16, fontweight='bold', pad=10)

x_values = Total_sales_by_outlet_establishment.index.tolist()
y_values = Total_sales_by_outlet_establishment.values.tolist()

for x, y in zip(x_values, y_values):
    plt.text(x, y + (max(y_values) * 0.02),  
             f'{y/1000:,.0f}K',
             ha='center',
             fontsize=9,
             fontweight='bold',
             color='#00A859')

plt.tight_layout()
plt.savefig(f"{plot_path}Total Sales by Outlet Establishment.png",dpi=300,bbox_inches='tight')
plt.show()




# # 5. Sales by Outlet Size:
# # 	Objective: Analyze the correlation between outlet size and total sales.
# # 	Chart Type: Donut/ Pie Chart.

Sales_by_Outlet_Size = var1.groupby("Outlet Size")["Sales"].sum()

plt.title("Sales by Outlet Size", fontsize=16, fontweight="bold")
plt.xlabel("Outlet Size",fontsize=12, fontweight="bold")

plt.pie(Sales_by_Outlet_Size, labels= Sales_by_Outlet_Size.index,
              colors = blinkit_palette,
               autopct="%1.1f%%", wedgeprops={'edgecolor': 'black', 'linewidth': 1},
                textprops={'color': 'black', 'fontweight': 'bold', 'fontsize': 10})

plt.tight_layout()
plt.savefig(f"{plot_path}Sales by Outlet Size.png",dpi=300,bbox_inches='tight')
plt.show()



# # 6. Sales by Outlet Location:
# # 	Objective: Assess the geographic distribution of sales across different locations.
# # 	Chart Type: Funnel Map.

Sales_by_Outlet_Location = var1.groupby("Outlet Location Type")['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,4))
sns.barplot(y=Sales_by_Outlet_Location.index,
            x=Sales_by_Outlet_Location.values,
            hue=Sales_by_Outlet_Location.index,
            legend=False, palette=blinkit_palette,edgecolor='black')
plt.title("Sales by Outlet Location", fontsize=16, fontweight="bold", pad= 10)
plt.xlabel("Sales",fontsize=12, fontweight="bold", labelpad= 10)
plt.ylabel("Outlet Location Type",fontsize=12, fontweight="bold", labelpad= 10)

plt.tight_layout()
plt.savefig(f"{plot_path}Sales by Outlet Location.png",dpi=300,bbox_inches='tight')
plt.show()
