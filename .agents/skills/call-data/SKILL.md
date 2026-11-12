---
name: call-data
description: Composite bundler skill activating data engineering and database skills. Use for ETL data pipelines, SQL query tuning, schema modeling, PostgreSQL, dbt transformations, and Spark jobs.
---

# 🚀 Composite Skill: Big Data, Data Engineering & Databases (`/call-data`)

This composite skill drives enterprise data pipelines, modern data stack transformations (dbt), high-performance PostgreSQL tuning, Spark data processing, and data quality frameworks.

---

## 📦 Bundled Skills & Deep References

When detailed implementation schemas, dbt transformation rules, or specific database configurations are required, read the corresponding skill by reading its `SKILL.md` file:

| Skill | Path | Focus & On-Demand Capabilities |
| :--- | :--- | :--- |
| **`/data-engineer`** | `.agents/skills/data-engineer/SKILL.md` | Data warehouse design, streaming architectures, Airflow/Kafka |
| **`/data-engineering-data-pipeline`** | `.agents/skills/data-engineering-data-pipeline/SKILL.md` | Batch & streaming ETL/ELT pipelines, fault-tolerance |
| **`/data-quality-frameworks`** | `.agents/skills/data-quality-frameworks/SKILL.md` | Great Expectations, dbt tests, data contracts, anomaly checks |
| **`/database-architect`** | `.agents/skills/database-architect/SKILL.md` | Relational, column-family & time-series database design |
| **`/database-optimizer`** | `.agents/skills/database-optimizer/SKILL.md` | Query optimization, connection pooling, cache tiers |
| **`/sql-optimization-patterns`** | `.agents/skills/sql-optimization-patterns/SKILL.md` | `EXPLAIN (ANALYZE, BUFFERS)` inspection, index tuning |
| **`/database-migration`** | `.agents/skills/database-migration/SKILL.md` | Zero-downtime database migrations, rollback protocols |
| **`/postgresql`** | `.agents/skills/postgresql/SKILL.md` | Postgres indexing (GIN, BRIN, GiST), JSONB, partitioning |
| **`/sql-pro`** | `.agents/skills/sql-pro/SKILL.md` | Advanced SQL, window functions, CTEs, OLAP optimizations |
| **`/dbt-transformation-patterns`** | `.agents/skills/dbt-transformation-patterns/SKILL.md` | Staging/Intermediate/Mart models, incremental strategies |
| **`/spark-optimization`** | `.agents/skills/spark-optimization/SKILL.md` | Spark partitioning, broadcast hash joins, memory tuning |
| **`/data-engineering-data-driven-feature`** | `.agents/skills/data-engineering-data-driven-feature/SKILL.md` | Build features guided by data insights, A/B testing, and continuous measurement using… |
| **`/database-admin`** | `.agents/skills/database-admin/SKILL.md` | Expert database administrator specializing in modern cloud databases, automation, and… |

---

## ⚡ Core Directives & Playbook (Fast Path)

When `/call-data` is invoked, strictly adhere to these data architecture standards:

### 1. Medallion Data Architecture (ELT/ETL)
- **Bronze (Raw)**: Append-only raw ingested events/tables preserving original format and ingestion metadata.
- **Silver (Cleaned & Conformed)**: Deduplicated, type-casted, schema-enforced, and normalized domain tables.
- **Gold (Aggregated & Marts)**: Dimensional models (Star schema) or wide feature tables optimized for BI and analytics.

### 2. dbt Modeling & Materialization Rules
- **Layering**: `staging/` (views with `stg_` prefix) ➔ `intermediate/` (ephemeral/view `int_` prefix) ➔ `marts/` (table/incremental `fct_` or `dim_` prefix).
- **Incremental Strategy**: Use `unique_key` and merge strategies for high-volume incremental tables:
  ```sql
  {{ config(materialized='incremental', unique_key='id', on_schema_change='append_new_columns') }}
  SELECT * FROM source_events
  {% if is_incremental() %}
    WHERE updated_at > (SELECT MAX(updated_at) FROM {{ this }})
  {% endif %}
  ```

### 3. PostgreSQL Performance & Indexing
- **Index Selection**:
  - `B-Tree`: Equality and range queries on high-cardinality columns.
  - `GIN`: Full-text search and JSONB containment (`@>`).
  - `BRIN`: Naturally ordered, append-only time-series data on huge tables.
  - `Partial Index`: Filtered queries (e.g. `WHERE status = 'pending'`).
- **Query Optimization**: Always test query plans with `EXPLAIN (ANALYZE, BUFFERS)` to verify zero sequential scans on large datasets.

### 4. Data Quality & Idempotency
- All ETL/ELT pipelines must be strictly **idempotent** (re-running the same pipeline produces identical state).
- Enforce primary key uniqueness, non-null constraints, and referential integrity tests at every stage.

---

## ⚡ Execution Workflow

1. **Schema & Pipeline Architecture**: Model data contracts, entity relationships, and ingestion cadence.
2. **Transformations & Optimization**: Write SQL/dbt models or Spark jobs, configure indexes, and eliminate query bottlenecks.
3. **Data Quality & Validation**: Run data tests (dbt test / Great Expectations), verify schema contracts, and validate pipeline output.
