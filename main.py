import streamlit as st
from campaign import handle_campaign_details
from apollo import handle_icp_details
from send_email import send_email
import pandas as pd

test_people = [{'first_name': 'Anthony', 'last_name': 'James', 'organization_name': 'Trinity Consulting Services', 'linkedin_url': 'http://www.linkedin.com/in/ajjames', 'email' : 'harshit.leadcured@gmail.com'}]

# Page layout
def main():
    st.title("ICP and Campaign Form")

    if "icp_submitted" not in st.session_state:
        st.session_state.icp_submitted = False
    if "campaign_submitted" not in st.session_state:
        st.session_state.campaign_submitted = False

    # Step 1: Fill ICP form
    if not st.session_state.icp_submitted:
        with st.form("icp_form"):
            st.header("ICP Details")
            person_titles = st.text_area("Person Titles (comma-separated)", placeholder='e.g. "sales director, engineer manager"')
            q_keywords = st.text_input("Query Keywords", placeholder='e.g. "Tim"')
            prospected_by_current_team = st.multiselect("Prospected by Current Team", ["yes", "no"])
            person_locations = st.text_area("Person Locations (comma-separated)", placeholder='e.g. "California, US, Minnesota, US"')
            person_seniorities = st.text_area("Person Seniorities (comma-separated)", placeholder='e.g. "senior, manager"')
            contact_email_status = st.text_area("Contact Email Status (comma-separated)", placeholder='e.g. "verified, guessed, unavailable, bounced, pending_manual_fulfillment"')
            q_organization_domains = st.text_area("Organization Domains (newline-separated)", placeholder='e.g. "google.com\nfacebook.com"')
            organization_locations = st.text_area("Organization Locations (comma-separated)", placeholder='e.g. "California, US, Minnesota, US"')
            organization_ids = st.text_area("Organization IDs (comma-separated)", placeholder='e.g. "63ff0bc1ff57ba0001e7eXXX"')
            organization_num_employees_ranges = st.text_area("Organization Employee Ranges (comma-separated)", placeholder='e.g. "1,10, 101,200"')
            page = st.number_input("Page", min_value=1, value=1)
            per_page = st.number_input("Results per Page", min_value=1, max_value=100, value=10)
            
            icp_submit = st.form_submit_button("Submit ICP")

        if icp_submit:
            st.session_state.icp_submitted = True
            st.session_state.icp_details = {
                "person_titles": [title.strip() for title in person_titles.split(",")] if person_titles else [],
                "q_keywords": q_keywords,
                "prospected_by_current_team": prospected_by_current_team,
                "person_locations": [location.strip() for location in person_locations.split(",")] if person_locations else [],
                "person_seniorities": [seniority.strip() for seniority in person_seniorities.split(",")] if person_seniorities else [],
                "contact_email_status": [status.strip() for status in contact_email_status.split(",")] if contact_email_status else [],
                "q_organization_domains": q_organization_domains.split("\n") if q_organization_domains else [],
                "organization_locations": [location.strip() for location in organization_locations.split(",")] if organization_locations else [],
                "organization_ids": [org_id.strip() for org_id in organization_ids.split(",")] if organization_ids else [],
                "organization_num_employees_ranges": [range.strip() for range in organization_num_employees_ranges.split(",")] if organization_num_employees_ranges else [],
                "page": page,
                "per_page": per_page
            }
            st.experimental_rerun()

    # Step 2: Select campaign type
    if st.session_state.icp_submitted and not st.session_state.campaign_submitted:
        st.header("Select Campaign Type")
        campaign_type = st.selectbox("Campaign Type", ["USP Based", "Discount Offer", "New Solution Launch"])

        # Step 3: Fill campaign-specific form
        with st.form("campaign_form"):
            st.header(f"{campaign_type} Details")
            sender_name = st.text_input("Sender's Name", placeholder="Representative from your company")
            sender_organization = st.text_input("Sender's Organization", placeholder="Your company")
            product_service = st.text_input("Product/Service", placeholder="Unique solution or feature offered by your company")
            industry = st.text_input("Industry", placeholder="Relevant industry of the recipient")
            
            campaign_details = {
                "type": campaign_type,
                "sender_name": sender_name,
                "sender_organization": sender_organization,
                "product_service": product_service,
                "industry": industry
            }
            
            campaign_submit = st.form_submit_button("Submit Campaign")

        if campaign_submit:
            st.session_state.campaign_submitted = True
            st.session_state.campaign_details = campaign_details
            st.experimental_rerun()

    # Step 4: Handle ICP and campaign details and display results
    if st.session_state.icp_submitted and st.session_state.campaign_submitted:
        people_list = handle_icp_details(st.session_state.icp_details)
        subject,body = handle_campaign_details(st.session_state.campaign_details)

        st.header("Results")
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(people_list)

        # Rename columns
        df.columns = ["Full Name", "Email", "Organization Name"]

        # Set the index to start from 1
        df.index = range(1, len(df) + 1)

        # Display the DataFrame as a table in Streamlit
        st.write("List of People:")
        st.table(df)

        st.write("Email Content:")
        st.text_area("Email subject", subject, height=100)
        st.text_area("Email body", body, height=800)


        # Step 6: Send email button
        if st.button("Start Sending Emails"):
            send_email(test_people , subject, body)
            st.success("Emails sent successfully!")

if __name__ == "__main__":
    main()
