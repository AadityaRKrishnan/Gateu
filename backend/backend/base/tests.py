def filter_nic_details(account, nic_id, page_number, page_limit, exclude_accounts, filters, org_Units):
    if len(account) == 0 and org_Units == 'ALL':
        filter_data = {
            "nic_id": nic_id
        }
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
                sub_filter = {}

            filter_data.update(sub_filter)

    elif len(account) > 0 and org_Units == 'ALL' and exclude_accounts == False:
        filter_data = {
            "nic_data.aws_account_id": {
                '$in': account
            },
            "nic_id": nic_id
        }
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
                sub_filter = {}

            filter_data.update(sub_filter)
    elif len(account) > 0 and org_Units != 'ALL' and exclude_accounts == False:
        filter_data = {
            "nic_data.aws_account_id": {
                '$in': account
            },
            "nic_id": nic_id,
            "nic_data.org_unit_id": org_Units
        }
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
                sub_filter = {}

            filter_data.update(sub_filter)
    elif len(account) == 0 and org_Units != 'ALL' and exclude_accounts == False:
        filter_data = {
            "nic_id": nic_id,
            "nic_data.org_unit_id": org_Units
        }
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
                sub_filter = {}

            filter_data.update(sub_filter)
    elif len(account) > 0 and org_Units == 'ALL' and exclude_accounts == True:
        filter_data = {
            "nic_data.aws_account_id": {
                '$nin': account
            },
            "nic_id": nic_id
        }
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
                sub_filter = {}

            filter_data.update(sub_filter)
    elif len(account) > 0 and org_Units != 'ALL' and exclude_accounts == True:
        filter_data = {
            "nic_data.aws_account_id": {
                '$nin': account
            },
            "nic_id": nic_id,
            "nic_data.org_unit_id": org_Units
        }
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
                sub_filter = {}

            filter_data.update(sub_filter)

    elif len(account) == 0 and org_Units != 'ALL' and exclude_accounts == True:
        filter_data = {
            "nic_id": nic_id,
            "nic_data.org_unit_id": org_Units
        }
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
                sub_filter = {}

            filter_data.update(sub_filter)

    response = filter_collection(collection_name, filter_data, int(page_number), int(page_limit))
    if response:
        return response
