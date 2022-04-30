--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: faculty; Type: TABLE; Schema: public; Owner: aika
--

CREATE TABLE public.faculty (
    id integer NOT NULL,
    title character varying(50)
);


ALTER TABLE public.faculty OWNER TO aika;

--
-- Name: faculty_id_seq; Type: SEQUENCE; Schema: public; Owner: aika
--

CREATE SEQUENCE public.faculty_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.faculty_id_seq OWNER TO aika;

--
-- Name: faculty_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: aika
--

ALTER SEQUENCE public.faculty_id_seq OWNED BY public.faculty.id;


--
-- Name: students; Type: TABLE; Schema: public; Owner: aika
--

CREATE TABLE public.students (
    id integer NOT NULL,
    name character varying(50),
    last_name character varying(50),
    faculty_id integer
);


ALTER TABLE public.students OWNER TO aika;

--
-- Name: students_id_seq; Type: SEQUENCE; Schema: public; Owner: aika
--

CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.students_id_seq OWNER TO aika;

--
-- Name: students_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: aika
--

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;


--
-- Name: faculty id; Type: DEFAULT; Schema: public; Owner: aika
--

ALTER TABLE ONLY public.faculty ALTER COLUMN id SET DEFAULT nextval('public.faculty_id_seq'::regclass);


--
-- Name: students id; Type: DEFAULT; Schema: public; Owner: aika
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);


--
-- Data for Name: faculty; Type: TABLE DATA; Schema: public; Owner: aika
--

COPY public.faculty (id, title) FROM stdin;
1	Medicine
2	IT
3	Business
4	Psychology
5	History
6	Economics
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: aika
--

COPY public.students (id, name, last_name, faculty_id) FROM stdin;
1	John	Snow	3
2	Alice	Pumpkin	1
3	Chris	White	4
4	Emily	Baker	2
5	Bob	Smith	2
6	Emily	Justice	4
8	Tom	Jerry	\N
\.


--
-- Name: faculty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: aika
--

SELECT pg_catalog.setval('public.faculty_id_seq', 6, true);


--
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: aika
--

SELECT pg_catalog.setval('public.students_id_seq', 8, true);


--
-- Name: faculty faculty_pkey; Type: CONSTRAINT; Schema: public; Owner: aika
--

ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY (id);


--
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: aika
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- Name: student_faculty_id_index; Type: INDEX; Schema: public; Owner: aika
--

CREATE INDEX student_faculty_id_index ON public.students USING btree (faculty_id);


--
-- Name: students fk_students_faculty; Type: FK CONSTRAINT; Schema: public; Owner: aika
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT fk_students_faculty FOREIGN KEY (faculty_id) REFERENCES public.faculty(id);


--
-- PostgreSQL database dump complete
--

