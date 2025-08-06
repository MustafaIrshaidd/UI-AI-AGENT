-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create jobs table
CREATE TABLE IF NOT EXISTS jobs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    company VARCHAR(255),
    location VARCHAR(255),
    salary_min INTEGER,
    salary_max INTEGER,
    job_type VARCHAR(50), -- full-time, part-time, contract, etc.
    status VARCHAR(50) DEFAULT 'active', -- active, closed, draft
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create applications table
CREATE TABLE IF NOT EXISTS applications (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    job_id UUID REFERENCES jobs(id) ON DELETE CASCADE,
    status VARCHAR(50) DEFAULT 'pending', -- pending, accepted, rejected, withdrawn
    applied_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, job_id)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_jobs_status ON jobs(status);
CREATE INDEX IF NOT EXISTS idx_applications_user_id ON applications(user_id);
CREATE INDEX IF NOT EXISTS idx_applications_job_id ON applications(job_id);

-- Insert sample data
INSERT INTO users (email, username, full_name) VALUES
    ('john.doe@example.com', 'johndoe', 'John Doe'),
    ('jane.smith@example.com', 'janesmith', 'Jane Smith')
ON CONFLICT (email) DO NOTHING;

INSERT INTO jobs (title, description, company, location, salary_min, salary_max, job_type) VALUES
    ('Senior Python Developer', 'We are looking for an experienced Python developer...', 'TechCorp', 'San Francisco, CA', 120000, 180000, 'full-time'),
    ('Frontend React Developer', 'Join our team to build amazing user interfaces...', 'StartupXYZ', 'Remote', 80000, 120000, 'full-time'),
    ('DevOps Engineer', 'Help us scale our infrastructure...', 'BigTech Inc', 'New York, NY', 100000, 150000, 'full-time')
ON CONFLICT DO NOTHING; 