import os
from DrissionPage import ChromiumPage, ChromiumOptions
import time






    # Initialize the browser
driver = ChromiumPage()

# Open the target website
driver.get('https://app.apollo.io/#/login')

time.sleep(15)
list=driver.ele('#side-nav-lists')
list.click()
time.sleep(15)
parent = driver.ele('#table-row-2')
# Find the <a> tag within the parent element
time.sleep(5)
test = parent.ele('.zp_p2Xqs zp_v565m zp_vJPW7')
test.click()
time.sleep(5)
checkbox = driver.ele('.zp_zzdNt')
checkbox=driver.ele('.zp_qe0Li zp_S5tZC zp_iRsfd')
if checkbox:
        # Click the first matching checkbox
    checkbox.click()
    print("Checkbox clicked successfully.")
else:
    print("No checkbox with aria-checked='true' found.")
apply_button = driver.ele('.zp_qe0Li zp_FG3Vz zp_rsjqe zp_h2EIO')
# apply_button = driver.ele('div.zp_uzcP0 button:nth-child(2)')
if apply_button:
    apply_button.click()
    print("Apply button clicked successfully.")
else:
    print("Apply button not found.")

time.sleep(5)
child=driver.ele('.zp-icon apollo-icon apollo-icon-enrichment-refresh zp_QUSTG zp_D0r3Q zp_K7tmh zp_NGTfw')
if child:
    child.click()
    print("Enrich clicked successfully.")
else:
    print("Enrich not found.")
Enrich_email=driver.ele('.zp_Y9mcf')
if Enrich_email:
    Enrich_email.click()
    print("Enrich email clicked successfully.")
else:
    print("Enrich email not found.")
Email=driver.ele('.zp-button zp_GGHzP zp_Kbe5T')
if Email:
    Email.click()
    print("Email clicked successfully.")
else:
    print("Email not found.")
time.sleep(5)
# for i in range(100):
#     print(f"Iteration {i + 1} started.")

#     checkbox = driver.ele('.zp_qe0Li zp_S5tZC zp_iRsfd')
#     if checkbox:
#         checkbox.click()
#         print("Checkbox clicked successfully.")
#     else:
#         print("No checkbox with aria-checked='true' found.")
#     time.sleep(2)  # Wait before proceeding
#     apply_button = driver.ele('.zp_qe0Li zp_FG3Vz zp_rsjqe zp_h2EIO')
#     if apply_button:
#         apply_button.click()
#         print("Apply button clicked successfully.")
#     else:
#         print("Apply button not found.")

#     time.sleep(5)  # Wait before proceeding

#     child = driver.ele('.zp-icon apollo-icon apollo-icon-enrichment-refresh zp_QUSTG zp_D0r3Q zp_K7tmh zp_NGTfw')
#     if child:
#         child.click()
#         print("Enrich clicked successfully.")
#     else:
#         print("Enrich not found.")
#     time.sleep(2)  # Wait before proceeding
#     Enrich_email = driver.ele('.zp_Y9mcf')
#     if Enrich_email:
#         Enrich_email.click()
#         print("Enrich email clicked successfully.")
#     else:
#         print("Enrich email not found.")

#     Email = driver.ele('.zp-button zp_GGHzP zp_Kbe5T')
#     if Email:
#         Email.click()
#         print("Email clicked successfully.")
#     else:
#         print("Email not found.")

#     time.sleep(5)  # Wait before the next iteration
#     print(f"Iteration {i + 1} completed.\n")