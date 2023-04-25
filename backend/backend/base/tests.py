import React, { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table';
import { Button } from 'react-bootstrap';
import Pagination from 'react-bootstrap/Pagination';
import FurtherModal from './FurtherModal';

 function PaginatedTable(props) {
 const {nicRecords, datatable_configurations} = props;

  // Initialize the state variables with useState Hook
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(0);
  const [pageData, setPageData] = useState([]);
  const [rowsPerPage, setRowsPerPage] = useState(5); // initialize rows per page with 5
  const [showModal, setShowModal] = useState(false);

  // Define a useEffect Hook to fetch the data for the current page
  useEffect(() => {
    // Calculate the total number of pages
    setTotalPages(Math.ceil(nicRecords.data.length / rowsPerPage));
    // Calculate the start and end indices of the data slice
    const startIndex = (currentPage - 1) * rowsPerPage;
    const endIndex = startIndex + rowsPerPage;
    // Set the sliced data as the page data
    setPageData(nicRecords.data.slice(startIndex, endIndex));
  }, [currentPage, rowsPerPage]); // add rowsPerPage to dependency array

  const handleOpenModal = () => {
    setShowModal(true);
  }

  const handleCloseModal = () => {
    setShowModal(false);
  }

  // Define a helper function to handle previous button click
  function handlePrevClick() {
    // Decrease the current page number by one if it is not the first page
    if (currentPage > 1) {
      setCurrentPage((prevPage) => prevPage - 1);
    }
  }

  // Define a helper function to handle next button click
  function handleNextClick() {
    // Increase the current page number by one if it is not the last page
    if (currentPage < totalPages) {
      setCurrentPage((prevPage) => prevPage + 1);
    }
  }

  // Define a helper function to handle page number click
  function handlePageClick(number) {
    // Set the current page number to the clicked number
    setCurrentPage(number);
  }

  // Define a helper function to get the pagination items
  function getPaginationItems() {
    // Initialize an empty array for storing the pagination items
    const items = [];
    // Loop through each page number and create a pagination item
    for (let number = 1; number <= totalPages; number++) {
      items.push(
        <Pagination.Item
          key={number}
          active={number === currentPage}
          onClick={() => handlePageClick(number)}
        >
          {number}
        </Pagination.Item>
      );
    }
    // Return the pagination items
    return items;
  }

  // Define a helper function to handle rows per page change
  function handleRowsPerPageChange(event) {
    // Update the rows per page value
    setRowsPerPage(parseInt(event.target.value));
    // Reset the current page to 1
    setCurrentPage(1);
  }
  return (
    <div className="container">
  <div className="row mb-3">
    <div className="col-md-6">
      <div className="d-flex align-items-center">
        <span>Show</span>
        <select className="ml-2" value={rowsPerPage} onChange={handleRowsPerPageChange}>
          <option value="5">5</option>
          <option value="10">10</option>
          <option value="25">25</option>
          <option value="50">50</option>
        </select>
        <span className="ml-2">records per page</span>
      </div>
    </div>
    <div className="col-md-6">
      <div className="d-flex justify-content-end">
        <Pagination>
          <Pagination.Prev onClick={handlePrevClick} />
          {getPaginationItems()}
          <Pagination.Next onClick={handleNextClick} />
        </Pagination>
      </div>
    </div>
  </div>
  <Table className="table table-striped table-bordered table-hover">
    <thead>
      <tr>
        <th>Account</th>
        <th>Organization Unit</th>
        <th>action</th>
      </tr>
    </thead>
    <tbody>
      {pageData.map((row) => (
        <tr key={row.id}>
          <td>{row.aws_account_id.account_name}</td>
          <td>{row.org_id.org_unit_name}</td>
          <td><Button onClick={handleOpenModal}>More</Button></td>
          <FurtherModal key={row.id} showModal={showModal} moreData={row.more_details} nic_type={nicRecords.nic_type} handleCloseModal={handleCloseModal} org_account_name={ row.aws_account_id.account_name}/>
        </tr>
      ))}
    </tbody>
  </Table>
</div>

  );
}

// Export the component
export default PaginatedTable;
