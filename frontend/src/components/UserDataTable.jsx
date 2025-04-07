import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios";

const UserDataTable = () => {
  const [data, setData] = useState([]); 
  const [loading, setLoading] = useState(true);
  const [selectedUser, setSelectedUser] = useState(null); 
  const [showEditModal, setShowEditModal] = useState(false); 
  const [showDeleteModal, setShowDeleteModal] = useState(false); 

  // Configuración de columnas
  const columns = [
    {
      name: "Nombre",
      selector: (row) => row.name,
      sortable: true,
    },
    {
      name: "Email",
      selector: (row) => row.email,
      sortable: true,
    },
    {
      name: "Teléfono",
      selector: (row) => row.tel,
    },
    {
      name: "Acciones",
      cell: (row) => (
        <span>
          <button
            className="btn btn-warning me-4"
            onClick={() => handleEdit(row)}
          >
            <i className="bi bi-pencil"></i>
          </button>
          <button
            className="btn btn-danger me-4"
            onClick={() => handleDelete(row,
              row.email
            )}
          >
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error al cargar los datos:", error);
        setLoading(false);
      });
  }, []);

  const handleEdit = (user) => {
    setSelectedUser(user);
    setShowEditModal(true);
  };

  const handleEditSubmit = () => {
    if (!selectedUser || !selectedUser.id) {
      console.error("El usuario seleccionado no tiene un ID válido.");
      return;
    }
  
    console.log("Datos enviados para actualizar:", selectedUser);
  
    axios
      .put(`http://127.0.0.1:8000/users/api/${selectedUser.id}/`, selectedUser,
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
          },
        }
      )
      .then((response) => {
        setData(
          data.map((item) =>
            item.id === selectedUser.id ? response.data : item
          )
        );
        setShowEditModal(false); 
        console.log("Usuario actualizado:", response.data);
      })
      .catch((error) => {
        console.error("Error al actualizar el usuario:", error.response || error);
      });
  };
  
  const handleDeleteConfirm = () => {
    if (!selectedUser || !selectedUser.id) {
      console.error("El usuario seleccionado no tiene un ID válido.");
      return;
    }

  
    axios
      .delete(`http://127.0.0.1:8000/users/api/${selectedUser.id}/`,{
        headers:{
          Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
        }
      })
      .then(() => {
        setData(data.filter((item) => item.id !== selectedUser.id));
        setShowDeleteModal(false);
        console.log("Usuario eliminado con éxito.");
      })
      .catch((error) => {
        console.error("Error al eliminar el usuario:", error.response || error);
      });
  };
  const handleDelete = (user,email) => {
    const currentUserEmail = localStorage.getItem("userEmail");
    console.log("Email del usuario actual:", currentUserEmail);
    console.log("Email del usuario seleccionado:", email);
    if (email === currentUserEmail) {
      alert("No puedes eliminar tu propio usuario.");
      return;
    }
    setSelectedUser(user);
    setShowDeleteModal(true);
  };

  return (
    <div>
      <h3>Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />

      {/* Modal de edición */}
      {showEditModal && (
        <div className="modal show d-block" tabIndex="-1">
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Editar Usuario</h5>
                <button
                  type="button"
                  className="btn-close"
                  onClick={() => setShowEditModal(false)}
                ></button>
              </div>
              <div className="modal-body">
                <div className="mb-3">
                  <label className="form-label">Nombre</label>
                  <input
                    type="text"
                    className="form-control"
                    value={selectedUser.name}
                    onChange={(e) =>
                      setSelectedUser({ ...selectedUser, name: e.target.value })
                    }
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Email</label>
                  <input
                    type="email"
                    className="form-control"
                    value={selectedUser.email}
                    onChange={(e) =>
                      setSelectedUser({ ...selectedUser, email: e.target.value })
                    }
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Teléfono</label>
                  <input
                    type="text"
                    className="form-control"
                    value={selectedUser.tel}
                    onChange={(e) =>
                      setSelectedUser({ ...selectedUser, tel: e.target.value })
                    }
                  />
                </div>
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => setShowEditModal(false)}
                >
                  Cancelar
                </button>
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={handleEditSubmit}
                >
                  Guardar Cambios
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Modal de eliminación */}
      {showDeleteModal && (
        <div className="modal show d-block" tabIndex="-1">
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Eliminar Usuario</h5>
                <button
                  type="button"
                  className="btn-close"
                  onClick={() => setShowDeleteModal(false)}
                ></button>
              </div>
              <div className="modal-body">
                <p>
                  ¿Estás seguro de que deseas eliminar al usuario{" "}
                  <strong>{selectedUser.name}</strong>?
                </p>
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => setShowDeleteModal(false)}
                >
                  Cancelar
                </button>
                <button
                  type="button"
                  className="btn btn-danger"
                  onClick={handleDeleteConfirm}
                >
                  Confirmar
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default UserDataTable;