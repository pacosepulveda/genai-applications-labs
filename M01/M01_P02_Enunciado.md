# M01.P02 — Del caso de uso a criterios de éxito

**Modalidad:** grupos de 3–4  
**Entregable:** ficha de caso de uso y primera matriz de riesgos

## Escenario

Trabajas para **Asteria Engineering**, una organización ficticia que desarrolla proyectos tecnológicos e industriales. Dispone de miles de procedimientos, especificaciones, manuales y documentos de proyecto. Los profesionales pierden tiempo localizando información, y en ocasiones aparecen documentos antiguos junto a versiones vigentes.

La dirección plantea varias ideas:

1. asistente para localizar y explicar documentación técnica autorizada;
2. generador automático de propuestas comerciales completas;
3. resumen de actas de reuniones;
4. decisión automática de promoción y evaluación de empleados;
5. clasificación y priorización de incidencias técnicas.

Tu equipo debe escoger **un caso de uso inicial** y transformarlo en un proyecto que pueda evaluarse.

## Tarea

Abre `notebooks/M01_P02_Use_Case_Canvas.ipynb` en el entorno web de laboratorio y completa:

### 1. Problema

Describe el problema actual sin mencionar todavía ninguna tecnología.

### 2. Usuario

¿Quién utiliza el sistema? ¿Quién se ve afectado por sus resultados?

### 3. Entrada y salida

Define:

- entradas;
- fuentes previstas;
- salida que espera el usuario;
- acciones que el sistema **no** debe ejecutar automáticamente.

### 4. Datos

Clasifica los datos que podría manejar la solución:

- públicos;
- internos;
- confidenciales;
- datos personales;
- propiedad intelectual;
- información contractual u otra información regulada.

### 5. Métricas

Define como mínimo:

- una métrica de negocio;
- una métrica de calidad;
- una métrica de riesgo o seguridad;
- una línea base con la que comparar.

### 6. Riesgos

Completa `assets/risk_register_template.csv` con al menos cinco riesgos.

### 7. Decisión

Concluye con una de estas decisiones:

- `GO`: candidato a prototipo;
- `GO_WITH_CONTROLS`: candidato, pero requiere controles antes de probarlo;
- `DEFER`: no es el primer caso que abordarías;
- `NO_GO`: no debería automatizarse de esta forma.

La decisión debe estar argumentada.

## Regla importante

No existe una puntuación matemática universal que decida por ti. Puedes utilizar la pequeña matriz del notebook para ordenar la discusión, pero **la decisión final debe estar razonada**.
