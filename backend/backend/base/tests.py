def filter_nic_details(account, nic_id, page_number, page_limit, exclude_accounts, filters, org_Units):
    filter_data = {"nic_id": nic_id}
    sub_filter = {}
    
    if nic_id == NetworkTypes.IGW.value:
        if filters["igw_filter"] == "all_igw_with_attachment":
            sub_filter = {
                "nic_data.igw_id": {"$ne": None},
                "nic_data.igw_data.Attachments.State": {"$eq": "available"}
            }
        elif filters["igw_filter"] == "all_igw_without_attachment":
            sub_filter = {
                "nic_data.igw_id": {"$eq": None},
                "nic_data.igw_data.Attachments.State": {"$ne": "available"}
            }
        elif filters["igw_filter"] == "all_igw_accounts":
            pass
        
    if len(account) > 0:
        filter_data["nic_data.aws_account_id"] = {"$in": account} if not exclude_accounts else {"$nin": account}
    
    if org_Units != 'ALL':
        filter_data["nic_data.org_unit_id"] = org_Units
        
    filter_data.update(sub_filter)
    
    return filter_data
