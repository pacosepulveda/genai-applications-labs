---
source_id: PROC-017
title: Procedimiento de acceso privilegiado
version: "3.2"
status: CURRENT
department: Security
classification: INTERNAL
effective_date: 2026-08-01
---

# PROC-017 — Procedimiento de acceso privilegiado

## 1. Alcance

Este procedimiento regula el acceso administrativo temporal a sistemas de producción.

## 2. Requisitos

Toda solicitud debe incluir:

- identificador del sistema;
- justificación de negocio;
- ventana temporal solicitada;
- responsable técnico.

El usuario debe utilizar MFA antes de activar el acceso.

## 3. Aprobaciones

El acceso requiere **dos aprobaciones**:

1. responsable directo del solicitante;
2. equipo de Seguridad.

Ninguna de las dos aprobaciones sustituye a la otra.

## 4. Duración

La concesión estándar tiene una duración máxima de **8 horas**.

Una ampliación requiere una nueva aprobación.

## 5. Emergencias

En un incidente P1, Seguridad puede autorizar un acceso temporal de emergencia. Debe regularizarse documentalmente antes del siguiente día laborable.

## 6. Auditoría

Todas las elevaciones de privilegios deben quedar registradas con usuario, sistema, fecha de inicio, fecha de fin y aprobadores.
